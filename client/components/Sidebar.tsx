'use client';

import { currentUser } from '@/lib/mock-data';
import { useAppSelector } from '@/store/hooks';

interface SidebarProps {
  activeId: string | null;
  onSelect: (id: string) => void;
}

export default function Sidebar({ activeId, onSelect }: SidebarProps) {
  const {briefs} = useAppSelector( s => s.chatBriefs )

  if(!briefs) return
  return (
    <aside className="flex h-full w-[300px] shrink-0 flex-col border-r border-line bg-paper-deep">
      <div className="px-5 pb-4 pt-6">
        <h1 className="font-display text-[1.35rem] italic leading-none text-ink">Ledger</h1>
        <p className="mt-1 text-xs uppercase tracking-[0.14em] text-ink-soft">Client conversations</p>
      </div>

     <nav className="flex-1 overflow-y-auto px-2 pb-2">
        {briefs.length === 0 ? (
          <EmptyChatList />
        ) : (
          <ul className="flex flex-col gap-0.5">
            {briefs.map((chat) => {
              const isActive = chat.id === activeId;
              return (
                <li key={chat.id}>
                  <button
                    onClick={() => onSelect(chat.id)}
                    className={`group relative flex w-full flex-col gap-0.5 rounded-md py-2.5 pl-3.5 pr-3 text-left transition-colors ${
                      isActive ? 'bg-ledger-soft' : 'hover:bg-black/[0.03]'
                    }`}
                  >
                    <span
                      className={`absolute left-0 top-2 h-[calc(100%-16px)] w-[3px] rounded-full transition-colors ${
                        isActive ? 'bg-ledger' : 'bg-transparent group-hover:bg-line'
                      }`}
                    />
                    <div className="flex items-center justify-between gap-2">
                      <span className={`truncate text-sm font-medium ${isActive ? 'text-ledger-deep' : 'text-ink'}`}>
                        {chat.name}
                      </span>
                      <span className="shrink-0 font-mono text-[0.65rem] text-ink-soft">{chat.last_time}</span>
                    </div>
                    <span className="truncate text-xs text-ink-soft">{chat.company}</span>
                    <div className="flex items-center justify-between gap-2">
                      <span className="truncate text-xs text-ink-soft/80">{chat.last_message}</span>
                      {chat.unread > 0 && (
                        <span className="flex h-4 min-w-4 shrink-0 items-center justify-center rounded-full bg-ledger px-1 font-mono text-[0.6rem] text-paper">
                          {chat.unread}
                        </span>
                      )}
                    </div>
                  </button>
                </li>
              );
            })}
          </ul>
        )}
      </nav>
 
      <UserOverlay />
    </aside>
  );
}
 
function EmptyChatList() {
  return (
    <div className="flex h-full flex-col items-center justify-center gap-3 px-6 py-10 text-center">
      <div className="flex h-11 w-11 items-center justify-center rounded-full border border-dashed border-line text-ink-soft">
        <ChatIcon />
      </div>
      <div>
        <p className="text-sm font-medium text-ink">No conversations yet</p>
        <p className="mt-1 text-xs leading-relaxed text-ink-soft">
          New client conversations will show up here as they come in.
        </p>
      </div>
    </div>
  );
}
 
function ChatIcon() {
  return (
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M21 11.5C21.0034 12.8199 20.6951 14.1219 20.1 15.3C19.3944 16.7118 18.3098 17.8992 16.9674 18.7293C15.6251 19.5594 14.0782 19.9994 12.5 20C11.1801 20.0035 9.87812 19.6951 8.7 19.1L3 21L4.9 15.3C4.30493 14.1219 3.99656 12.8199 4 11.5C4.00061 9.92179 4.44061 8.37488 5.27072 7.03258C6.10083 5.69028 7.28825 4.6056 8.7 3.90003C9.87812 3.30496 11.1801 2.99659 12.5 3.00003H13C15.0843 3.11502 17.053 3.99479 18.5291 5.47089C20.0052 6.94699 20.885 8.91568 21 11V11.5Z"
        stroke="currentColor"
        strokeWidth="1.6"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}
 
function UserOverlay() {
  return (
    <div className="border-t border-line bg-paper-deep/95 px-4 py-3 backdrop-blur-sm">
      <div className="flex items-center gap-3">
        <div className="flex h-8 w-8 shrink-0 items-center justify-center rounded-full bg-ledger-deep font-mono text-[0.7rem] text-paper">
          {currentUser.initials}
        </div>
        <div className="min-w-0 flex-1">
          <p className="truncate text-sm font-medium text-ink">{currentUser.name}</p>
          <p className="truncate text-[0.7rem] text-ink-soft">{currentUser.role}</p>
        </div>
        <button
          type="button"
          aria-label="Log out"
          title="Log out"
          className="flex h-8 w-8 shrink-0 items-center justify-center rounded-md text-ink-soft transition-colors hover:bg-rust-soft hover:text-rust"
        >
          <LogoutIcon />
        </button>
      </div>
    </div>
  );
}
 
function LogoutIcon() {
  return (
    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
      <path
        d="M15 17L20 12L15 7"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
      <path d="M20 12H9" stroke="currentColor" strokeWidth="1.8" strokeLinecap="round" strokeLinejoin="round" />
      <path
        d="M9 21H6C4.89543 21 4 20.1046 4 19V5C4 3.89543 4.89543 3 6 3H9"
        stroke="currentColor"
        strokeWidth="1.8"
        strokeLinecap="round"
        strokeLinejoin="round"
      />
    </svg>
  );
}