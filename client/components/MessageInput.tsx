'use client';

import { FormEvent, useState } from 'react';

interface MessageInputProps {
  chatId: string
}

export default function MessageInput({ chatId }: MessageInputProps) {
  const [value, setValue] = useState('');

  function handleSubmit(e: FormEvent) {
    e.preventDefault();
    const trimmed = value.trim();
    if (!trimmed) return;
    
    setValue('');
  }

  return (
    <form onSubmit={handleSubmit} className="flex items-end gap-2 border-t border-line bg-paper px-5 py-3.5">
      <textarea
        value={value}
        onChange={(e) => setValue(e.target.value)}
        onKeyDown={(e) => {
          if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSubmit(e);
          }
        }}
        rows={1}
        placeholder="Write a message…"
        className="max-h-32 flex-1 resize-none rounded-md border border-line bg-paper-deep/40 px-3.5 py-2.5 text-sm text-ink placeholder:text-ink-soft/70 focus:border-ledger focus:outline-none"
      />
      <button
        type="submit"
        disabled={!value.trim()}
        className="flex h-[42px] shrink-0 items-center gap-1.5 rounded-md bg-ledger px-4 text-sm font-medium text-paper transition-opacity hover:opacity-90 disabled:cursor-not-allowed disabled:opacity-40"
      >
        Send
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M4.5 12H19.5M19.5 12L13.5 6M19.5 12L13.5 18"
            stroke="currentColor"
            strokeWidth="2"
            strokeLinecap="round"
            strokeLinejoin="round"
          />
        </svg>
      </button>
    </form>
  );
}
