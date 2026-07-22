'use client';

import { ChatRecord, DocKind } from '@/lib/types';

interface ChatThreadProps {
  chat: ChatRecord;
  onSend: (text: string) => void;
  onOpenDocument: (kind: DocKind) => void;
  openDoc: DocKind | null;
}

export default function ChatThreadHeader({ chat, onOpenDocument, openDoc }: Omit<ChatThreadProps, 'onSend'>) {
  return (
    <header className="flex items-center justify-between gap-4 border-b border-line bg-paper px-6 py-4">
      <div className="min-w-0">
        <h2 className="truncate font-display text-lg text-ink">{chat.name}</h2>
        <p className="truncate text-xs text-ink-soft">{chat.company}</p>
      </div>
      <div className="flex shrink-0 gap-2">
        {(['proposal', 'quotation'] as DocKind[]).map((kind) => (
          <button
            key={kind}
            onClick={() => onOpenDocument(kind)}
            className={`flex items-center gap-1.5 rounded-md border px-3 py-1.5 text-xs font-medium capitalize transition-colors ${
              openDoc === kind
                ? 'border-ledger bg-ledger-soft text-ledger-deep'
                : 'border-line text-ink-soft hover:text-ink'
            }`}
          >
            <DocIcon />
            {kind}
            {chat.documents[kind] && <span className="h-1.5 w-1.5 rounded-full bg-ledger" aria-hidden />}
          </button>
        ))}
      </div>
    </header>
  );
}

export function MessageList({ chat }: { chat: ChatRecord }) {
  return (
    <div className="flex flex-1 flex-col gap-3 overflow-y-auto px-6 py-5">
      {chat.messages.map((msg) => {
        const isMe = msg.author === 'me';
        return (
          <div key={msg.id} className={`flex ${isMe ? 'justify-end' : 'justify-start'}`}>
            <div
              className={`max-w-[70%] rounded-lg px-3.5 py-2.5 text-sm leading-relaxed ${
                isMe ? 'bg-ledger text-paper' : 'bg-paper-deep text-ink'
              }`}
            >
              <p>{msg.text}</p>
              <p className={`mt-1 font-mono text-[0.6rem] ${isMe ? 'text-paper/70' : 'text-ink-soft'}`}>{msg.time}</p>
            </div>
          </div>
        );
      })}
    </div>
  );
}

function DocIcon() {
  return (
    <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M7 3H14L19 8V19C19 20.1046 18.1046 21 17 21H7C5.89543 21 5 20.1046 5 19V5C5 3.89543 5.89543 3 7 3Z"
        stroke="currentColor"
        strokeWidth="1.6"
        strokeLinejoin="round"
      />
      <path d="M14 3V8H19" stroke="currentColor" strokeWidth="1.6" strokeLinejoin="round" />
      <path d="M8.5 12H15.5M8.5 15.5H15.5" stroke="currentColor" strokeWidth="1.6" strokeLinecap="round" />
    </svg>
  );
}
