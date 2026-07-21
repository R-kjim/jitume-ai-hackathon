"use client";

import React from 'react';
import { useWorkflowStore } from '../store/useWorkflowStore';

export const Sidebar: React.FC = () => {
  const workflows = useWorkflowStore((state) => state.workflows);
  const activeWorkflowId = useWorkflowStore((state) => state.activeWorkflowId);
  const searchQuery = useWorkflowStore((state) => state.searchQuery);
  const setActiveWorkflowId = useWorkflowStore((state) => state.setActiveWorkflowId);
  const setSearchQuery = useWorkflowStore((state) => state.setSearchQuery);
  const addWorkflow = useWorkflowStore((state) => state.addWorkflow);

  const filteredWorkflows = workflows.filter(
    (wf) =>
      wf.clientName.toLowerCase().includes(searchQuery.toLowerCase()) ||
      wf.projectTitle.toLowerCase().includes(searchQuery.toLowerCase())
  );

  const activeWorkflows = filteredWorkflows.filter((wf) => wf.currentStation === 'review');
  const completedWorkflows = filteredWorkflows.filter((wf) => wf.currentStation === 'completed');

  return (
    <aside className="w-80 h-full bg-[#121318] border-r border-gray-800 flex flex-col shrink-0 text-gray-300 select-none">
      <div className="p-4 border-b border-gray-800 flex items-center justify-between">
        <div className="flex items-center gap-2 font-bold text-white text-sm">
          <div className="w-6 h-6 rounded bg-blue-600 flex items-center justify-center text-xs">
            📑
          </div>
          <span>JITUME WORKFLOW </span>
        </div>
      </div>

      <div className="p-3">
        <button
          onClick={addWorkflow}
          className="w-full py-2 px-3 rounded-lg bg-gray-800/80 hover:bg-gray-800 text-gray-200 text-xs font-semibold flex items-center justify-center gap-2 border border-gray-700/60 transition-colors"
        >
          <span>⊕</span> New Client Workflow
        </button>
      </div>

      <div className="px-3 pb-3">
        <input
          type="text"
          placeholder="Search clients or projects..."
          value={searchQuery}
          onChange={(e) => setSearchQuery(e.target.value)}
          className="w-full bg-[#0d0e12] border border-gray-800 rounded-lg px-3 py-1.5 text-xs text-white placeholder-gray-500 focus:outline-none focus:border-blue-500"
        />
      </div>

      <div className="flex-1 overflow-y-auto px-3 space-y-4 text-xs">
        <div>
          <div className="px-2 py-1 text-[10px] font-bold tracking-wider text-gray-500 uppercase">
            Active Workflows ({activeWorkflows.length})
          </div>
          <div className="space-y-1 mt-1">
            {activeWorkflows.map((wf) => (
              <button
                key={wf.id}
                onClick={() => setActiveWorkflowId(wf.id)}
                className={`w-full text-left p-2.5 rounded-lg border transition-all ${
                  activeWorkflowId === wf.id
                    ? 'bg-gray-800/90 border-gray-600 text-white'
                    : 'bg-transparent border-transparent hover:bg-gray-800/40 text-gray-400'
                }`}
              >
                <div className="font-semibold text-gray-200 truncate">{wf.clientName}</div>
                <div className="text-[11px] text-gray-500 truncate">{wf.projectTitle}</div>
              </button>
            ))}
          </div>
        </div>

        <div>
          <div className="px-2 py-1 text-[10px] font-bold tracking-wider text-gray-500 uppercase">
            Completed ({completedWorkflows.length})
          </div>
          <div className="space-y-1 mt-1">
            {completedWorkflows.map((wf) => (
              <button
                key={wf.id}
                onClick={() => setActiveWorkflowId(wf.id)}
                className={`w-full text-left p-2.5 rounded-lg border transition-all flex items-center justify-between ${
                  activeWorkflowId === wf.id
                    ? 'bg-gray-800/90 border-gray-600 text-white'
                    : 'bg-transparent border-transparent hover:bg-gray-800/40 text-gray-400'
                }`}
              >
                <div className="truncate">
                  <div className="font-semibold text-gray-200 truncate">{wf.clientName}</div>
                  <div className="text-[11px] text-gray-500 truncate">{wf.projectTitle}</div>
                </div>
                <span className="text-emerald-500 text-xs">✓</span>
              </button>
            ))}
          </div>
        </div>
      </div>
    </aside>
  );
};