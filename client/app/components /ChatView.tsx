"use client";

import React, { useState } from 'react';
import { ClientWorkflow, useWorkflowStore } from '../store/useWorkflowStore';

interface ChatViewProps {
  workflow: ClientWorkflow;
  onApproveWorkflow: () => void;
}

export const ChatView: React.FC<ChatViewProps> = ({ workflow, onApproveWorkflow }) => {
  const { data } = workflow;
  const isConnected = useWorkflowStore((state) => state.isConnected);
  const [inputMessage, setInputMessage] = useState('');

  const handleSendMessage = (e: React.FormEvent) => {
    e.preventDefault();
    if (!inputMessage.trim()) return;

    // Send logic or local state update can be handled here
    console.log('Sent message:', inputMessage);
    setInputMessage('');
  };

  return (
    <div className="flex flex-col h-full w-full overflow-hidden bg-[#0d0e12] text-white">
      {/* Top Header */}
      <header className="flex items-center justify-between px-6 py-4 border-b border-gray-800 bg-[#121318] shrink-0">
        <div className="flex items-center gap-3">
          <h1 className="text-lg font-bold text-white">{workflow.clientName}</h1>
          <span className="text-xs px-2.5 py-1 rounded-full bg-gray-800 text-gray-400 font-medium border border-gray-700">
            {workflow.projectTitle}
          </span>

          <div className="flex items-center gap-2 ml-4 px-3 py-1 rounded-full bg-gray-900 border border-gray-800 text-xs font-mono">
            <span
              className={`w-2 h-2 rounded-full ${
                isConnected ? 'bg-emerald-500 animate-pulse' : 'bg-rose-500'
              }`}
            />
            <span className={isConnected ? 'text-emerald-400' : 'text-rose-400'}>
              {isConnected ? 'WS Connected' : 'WS Offline'}
            </span>
          </div>
        </div>

        <button
          onClick={onApproveWorkflow}
          className={`flex items-center gap-2 px-4 py-2 rounded-lg text-sm font-medium transition-all ${
            data.approved
              ? 'bg-emerald-600 hover:bg-emerald-500 text-white'
              : 'bg-blue-600 hover:bg-blue-500 text-white'
          }`}
        >
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <polyline points="20 6 9 17 4 12" />
          </svg>
          <span>{data.approved ? 'Approved ✓' : 'Human Review & Approve'}</span>
        </button>
      </header>

      {/* Main Content & Message Area */}
      <div className="flex-1 overflow-y-auto p-6 space-y-6">
        <div className="text-xs font-semibold uppercase tracking-wider text-amber-400">
          ⚡ AI Unified Workflow Output
        </div>

        {/* AI Analysis Summary Card */}
        <div className="p-6 rounded-xl border border-gray-800 bg-[#14161d] space-y-4 shadow-lg max-w-5xl">
          <div className="flex items-center gap-3 border-b border-gray-800 pb-3">
            <div className="w-8 h-8 rounded-lg bg-purple-600/20 text-purple-400 flex items-center justify-center font-bold text-sm border border-purple-500/30 shrink-0">
              🤖
            </div>
            <h2 className="text-base font-semibold text-white">AI Analysis & Project Overview</h2>
          </div>

          {data.analysis && (
            <div className="space-y-1 text-sm text-gray-300 pl-2">
              <p><strong className="text-gray-100">Requirements:</strong> {data.analysis.requirements?.join(', ')}</p>
              <p>
                <strong className="text-gray-100">Budget:</strong> <span className="text-emerald-400 font-semibold">{data.analysis.budget}</span> |{' '}
                <strong className="text-gray-100">Timeline:</strong> <span className="text-amber-400 font-semibold">{data.analysis.timeline}</span>
              </p>
            </div>
          )}
        </div>

        {/* Chat Transcript Stream */}
        <div className="space-y-4 max-w-5xl">
          <div className="text-xs font-semibold uppercase tracking-wider text-gray-500">
            💬 Conversation Transcript
          </div>

          {data.transcriptMessages && data.transcriptMessages.length > 0 ? (
            data.transcriptMessages.map((msg) => (
              <div
                key={msg.id}
                className={`flex flex-col p-3 rounded-lg border max-w-2xl ${
                  msg.role === 'consultant'
                    ? 'bg-blue-950/30 border-blue-800/40 ml-auto'
                    : 'bg-gray-800/40 border-gray-700/40 mr-auto'
                }`}
              >
                <div className="flex items-center justify-between gap-4 text-xs text-gray-400 mb-1">
                  <span className="font-semibold text-gray-200">{msg.speaker}</span>
                  <span className="text-[10px]">{msg.timestamp}</span>
                </div>
                <p className="text-sm text-gray-200">{msg.text}</p>
              </div>
            ))
          ) : (
            <div className="text-xs text-gray-500 italic">No messages in this workflow conversation yet.</div>
          )}
        </div>
      </div>

      {/* CHAT INPUT BOX AT THE BOTTOM */}
      <div className="p-4 border-t border-gray-800 bg-[#121318] shrink-0">
        <form onSubmit={handleSendMessage} className="max-w-5xl mx-auto flex items-center gap-2">
          <input
            type="text"
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            placeholder="Type a message or instruction for the client/AI..."
            className="flex-1 bg-[#0d0e12] border border-gray-800 rounded-lg px-4 py-2.5 text-sm text-white placeholder-gray-500 focus:outline-none focus:border-blue-500 transition-colors"
          />
          <button
            type="submit"
            className="px-5 py-2.5 bg-blue-600 hover:bg-blue-500 text-white rounded-lg text-sm font-semibold transition-colors flex items-center gap-1 shrink-0"
          >
            <span>Send</span>
            <span>➔</span>
          </button>
        </form>
      </div>
    </div>
  );
};
