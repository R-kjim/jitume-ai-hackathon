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
        {
          id: 't2',
          speaker: 'Sarah (Client)',
          role: 'client',
          text: 'Our sales team spends too much time manually entering leads into the CRM.',
          timestamp: '10:03 AM',
        },
      ],
      analysis: {
        requirements: [
          'Automated CRM lead intake',
          'AI lead summary generator',
          'Real-time webhook routing',
        ],
        painPoints: [
          'Manual logging consumes 15 hours/week',
          'Delayed response times',
        ],
        budget: '$15,000',
        timeline: '6 Weeks',
      },
      brief: {
        executiveSummary:
          'Automate manual lead capture and sync via custom AI agents within a 6-week delivery timeframe.',
        recommendations: [
          'Deploy fine-tuned extraction model',
          'Set up automated email summaries',
        ],
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
        painPoints: ['High support ticket volume'],
        budget: '$8,500',
        timeline: '3 Weeks',
      },
      brief: {
        executiveSummary:
          'Deploy an automated support bot to handle tier-1 customer inquiries.',
        recommendations: [
          'Integrate chatbot with website',
          'Connect to company knowledge base',
        ],
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

export const useWorkflowStore = create<WorkflowState>((set) => ({
  workflows: INITIAL_WORKFLOWS,

  activeWorkflowId: 'wf-1',

  searchQuery: '',

  // Since we're using dummy data, pretend we're connected.
  isConnected: true,

  // No WebSocket required.
  initWebSocket: () => {
    console.log('Running with dummy data.');
  },

  setActiveWorkflowId: (id) =>
    set({
      activeWorkflowId: id,
    }),

  setSearchQuery: (query) =>
    set({
      searchQuery: query,
    }),

  approveWorkflow: (id) =>
    set((state) => ({
      workflows: state.workflows.map((workflow) =>
        workflow.id === id
          ? {
              ...workflow,
              currentStation: 'completed',
              data: {
                ...workflow.data,
                approved: true,
              },
            }
          : workflow
      ),
    })),

  addWorkflow: () => {
    const newWorkflow: ClientWorkflow = {
      id: `wf-${Date.now()}`,
      clientName: 'New Client',
      projectTitle: 'Discovery Session',
      currentStation: 'review',
      createdAt: new Date().toISOString().split('T')[0],
      data: {
        transcriptMessages: [],
        analysis: {},
        brief: {},
        approved: false,
      },
    };

    set((state) => ({
      workflows: [newWorkflow, ...state.workflows],
      activeWorkflowId: newWorkflow.id,
    }));
  },
}));
