"use client";

import React, { useEffect } from 'react';
import { useWorkflowStore } from './store/useWorkflowStore';
import { ChatView } from './components /ChatView';
import { Sidebar } from './components /Sidebar';

export default function Home() {
  const initWebSocket = useWorkflowStore((state) => state.initWebSocket);
  const workflows = useWorkflowStore((state) => state.workflows);
  const activeWorkflowId = useWorkflowStore((state) => state.activeWorkflowId);
  const approveWorkflow = useWorkflowStore((state) => state.approveWorkflow);

  useEffect(() => {
    initWebSocket();
  }, [initWebSocket]);

  const activeWorkflow = workflows.find((wf) => wf.id === activeWorkflowId) || workflows[0];

  return (
    <div className="flex h-screen w-screen overflow-hidden bg-[#0d0e12]">
      <Sidebar />
      <main className="flex-1 h-full overflow-hidden">
        {activeWorkflow ? (
          <ChatView
            workflow={activeWorkflow}
            onApproveWorkflow={() => approveWorkflow(activeWorkflow.id)}
          />
        ) : (
          <div className="flex items-center justify-center h-full text-gray-500">
            Select a workflow to get started
          </div>
        )}
      </main>
    </div>
  );
}
