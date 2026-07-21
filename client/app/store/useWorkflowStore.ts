import { create } from 'zustand';

export interface TranscriptMessage {
  id: string;
  speaker: string;
  role: 'consultant' | 'client';
  text: string;
  timestamp: string;
}

export interface AnalysisData {
  requirements?: string[];
  painPoints?: string[];
  budget?: string;
  timeline?: string;
}

export interface BriefData {
  executiveSummary?: string;
  recommendations?: string[];
}

export interface WorkflowData {
  transcriptMessages?: TranscriptMessage[];
  analysis?: AnalysisData;
  brief?: BriefData;
  approved: boolean;
}

export interface ClientWorkflow {
  id: string;
  clientName: string;
  projectTitle: string;
  currentStation: 'review' | 'completed';
  createdAt: string;
  data: WorkflowData;
}

let socket: WebSocket | null = null;
let reconnectTimer: NodeJS.Timeout | null = null;

const INITIAL_WORKFLOWS: ClientWorkflow[] = [
  {
    id: 'wf-1',
    clientName: 'Acme Corp Call',
    projectTitle: 'AI Lead Capture Pipeline',
    currentStation: 'review',
    createdAt: '2026-07-20',
    data: {
      transcriptMessages: [
        {
          id: 't1',
          speaker: 'Alex (Consultant)',
          role: 'consultant',
          text: 'Thanks for joining today! Could you tell me a bit about your main operational bottlenecks right now?',
          timestamp: '10:02 AM',
        },
      ],
      analysis: {
        requirements: ['Automated CRM lead intake', 'AI lead summary generator', 'Real-time webhook routing'],
        painPoints: ['Manual logging consumes 15 hours/week', 'Delayed response times'],
        budget: '$15,000',
        timeline: '6 Weeks',
      },
      brief: {
        executiveSummary: 'Automate manual lead capture and sync via custom AI agents within a 6-week delivery timeframe.',
        recommendations: ['Deploy fine-tuned extraction model', 'Set up automated email summaries'],
      },
      approved: false,
    },
  },
  {
    id: 'wf-2',
    clientName: 'Starlight Retail',
    projectTitle: 'Customer Support Bot',
    currentStation: 'completed',
    createdAt: '2026-07-15',
    data: {
      transcriptMessages: [],
      analysis: {
        requirements: ['24/7 automated FAQ bot'],
        budget: '$8,500',
        timeline: '3 Weeks',
      },
      brief: {
        executiveSummary: 'Deploy an automated support bot to handle tier-1 customer inquiries.',
      },
      approved: true,
    },
  },
];

interface WorkflowState {
  workflows: ClientWorkflow[];
  activeWorkflowId: string;
  searchQuery: string;
  isConnected: boolean;

  initWebSocket: () => void;
  setActiveWorkflowId: (id: string) => void;
  setSearchQuery: (query: string) => void;
  approveWorkflow: (id: string) => void;
  addWorkflow: () => void;
}

export const useWorkflowStore = create<WorkflowState>((set, get) => ({
  workflows: INITIAL_WORKFLOWS,
  activeWorkflowId: 'wf-1',
  searchQuery: '',
  isConnected: false,

  initWebSocket: () => {
    if (socket && (socket.readyState === WebSocket.OPEN || socket.readyState === WebSocket.CONNECTING)) {
      return;
    }

    const connect = () => {
      if (reconnectTimer) clearTimeout(reconnectTimer);

      socket = new WebSocket('ws://localhost:8080');

      socket.onopen = () => {
        console.log('⚡ Connected to WebSocket server');
        set({ isConnected: true });
      };

      socket.onmessage = (event) => {
        try {
          const data = JSON.parse(event.data);
          if (data.type === 'WORKFLOW_APPROVED') {
            set((state) => ({
              workflows: state.workflows.map((wf) =>
                wf.id === data.workflowId
                  ? { ...wf, currentStation: 'completed', data: { ...wf.data, approved: true } }
                  : wf
              ),
            }));
          }
        } catch (err) {
          console.error('Error parsing WS message:', err);
        }
      };

      socket.onclose = () => {
        console.log('❌ Disconnected from WebSocket server');
        set({ isConnected: false });
        socket = null;
        reconnectTimer = setTimeout(connect, 3000);
      };

      socket.onerror = (err) => {
        console.error('WebSocket Error:', err);
      };
    };

    connect();
  },

  setActiveWorkflowId: (id) => set({ activeWorkflowId: id }),
  setSearchQuery: (query) => set({ searchQuery: query }),

  approveWorkflow: (id) => {
    if (socket && socket.readyState === WebSocket.OPEN) {
      socket.send(JSON.stringify({ type: 'WORKFLOW_APPROVED', workflowId: id }));
    }

    set((state) => ({
      workflows: state.workflows.map((wf) =>
        wf.id === id
          ? { ...wf, currentStation: 'completed', data: { ...wf.data, approved: true } }
          : wf
      ),
    }));
  },

  addWorkflow: () => {
    const newId = `wf-${Date.now()}`;
    const newWorkflow: ClientWorkflow = {
      id: newId,
      clientName: 'New Client Call',
      projectTitle: 'Discovery Phase',
      currentStation: 'review',
      createdAt: new Date().toISOString().split('T')[0],
      data: { transcriptMessages: [], approved: false },
    };

    set((state) => ({
      workflows: [newWorkflow, ...state.workflows],
      activeWorkflowId: newId,
    }));
  },
}));