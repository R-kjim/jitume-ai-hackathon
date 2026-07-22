'use client';

import { useMemo, useState } from 'react';
import { chats as initialChats } from '@/lib/mock-data';
import Sidebar from './Sidebar';
import MessageInput from './MessageInput';
import ChatThreadHeader, { MessageList } from './ChatThread';
import DocumentPanel from './DocumentPanel';
import { ChatRecord, DocKind } from '@/store/types';

export default function ChatApp() {
  const [chats, setChats] = useState<ChatRecord[]>(initialChats);
  const [activeId, setActiveId] = useState<string | null>(null);
  const [openDoc, setOpenDoc] = useState<DocKind | null>(null);

  const activeChat = useMemo(() => chats.find((c) => c.id === activeId)!, [chats, activeId]);

  function handleSelectChat(id: string) {
    setActiveId(id);
    setOpenDoc(null);
  }

  function handleSend(text: string) {
    const now = new Date();
    const time = now.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    setChats((prev) =>
      prev.map((c) =>
        c.id === activeId
          ? {
              ...c,
              lastMessage: text,
              lastTime: time,
              messages: [...c.messages, { id: `m${c.messages.length + 1}`, author: 'me', text, time }],
            }
          : c
      )
    );
  }

  function handleOpenDocument(kind: DocKind) {
    setOpenDoc((current) => (current === kind ? null : kind));
  }

  return (
    <div className="flex h-screen w-full overflow-hidden bg-paper">
      <Sidebar
        activeId={activeId}
        onSelect={handleSelectChat}
      />

      <main className="flex min-w-0 flex-1">
        <section className="flex min-w-0 flex-1 flex-col">
          <ChatThreadHeader 
            chat={activeChat} 
            onOpenDocument={handleOpenDocument} 
            openDoc={openDoc} 
          />
          <MessageList chat={activeChat} />
          <MessageInput chatId={activeChat.id} />
        </section>

        {openDoc && (
          <DocumentPanel
            active={openDoc}
            onChangeActive={setOpenDoc}
            documents={activeChat.documents}
            onClose={() => setOpenDoc(null)}
          />
        )}
      </main>
    </div>
  );
}
