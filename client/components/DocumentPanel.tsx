'use client';

import { DocKind, DocumentRecord } from '@/lib/types';

interface DocumentPanelProps {
  active: DocKind;
  onChangeActive: (kind: DocKind) => void;
  documents: Record<DocKind, DocumentRecord | null>;
  onClose: () => void;
}

const STATUS_STYLE: Record<DocumentRecord['status'], string> = {
  draft: 'bg-line/60 text-ink-soft',
  sent: 'bg-ledger-soft text-ledger-deep',
  accepted: 'bg-ledger text-paper',
};

export default function DocumentPanel({ active, onChangeActive, documents, onClose }: DocumentPanelProps) {
  const doc = documents[active];

  return (
    <div className="flex h-full w-[360px] shrink-0 flex-col border-l border-line bg-paper-deep">
      <div className="flex items-end gap-0 px-4 pt-4">
        {(['proposal', 'quotation'] as DocKind[]).map((kind) => {
          const isActive = kind === active;
          const has = Boolean(documents[kind]);
          return (
            <button
              key={kind}
              onClick={() => onChangeActive(kind)}
              className={`relative -mb-px flex items-center gap-1.5 rounded-t-md border border-b-0 px-4 py-2 text-sm capitalize transition-colors ${
                isActive
                  ? 'border-line bg-paper font-medium text-ink'
                  : 'border-transparent text-ink-soft hover:text-ink'
              }`}
              style={
                isActive
                  ? { boxShadow: 'inset 0 2px 0 0 #2B6E52' }
                  : undefined
              }
            >
              {kind}
              {!has && <span className="h-1 w-1 rounded-full bg-ink-soft/40" aria-hidden />}
            </button>
          );
        })}
        <button
          onClick={onClose}
          aria-label="Close document panel"
          title="Close"
          className="ml-auto mb-1.5 flex h-6 w-6 items-center justify-center rounded-md text-ink-soft hover:bg-black/[0.04] hover:text-ink"
        >
          <svg width="13" height="13" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
            <path
              d="M18 6L6 18M6 6L18 18"
              stroke="currentColor"
              strokeWidth="2"
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
        </button>
      </div>

      <div className="flex-1 overflow-y-auto border-t border-line bg-paper px-5 py-5">
        {doc ? (
          <DocumentDetail doc={doc} kind={active} />
        ) : (
          <EmptyDocument kind={active} />
        )}
      </div>
    </div>
  );
}

function DocumentDetail({ doc, kind }: { doc: DocumentRecord; kind: DocKind }) {
  return (
    <div className="flex flex-col gap-5">
      <div>
        <p className="font-mono text-[0.7rem] tracking-wide text-ink-soft">{doc.reference}</p>
        <h2 className="mt-1 font-display text-lg leading-snug text-ink">{doc.title}</h2>
        <span
          className={`mt-2 inline-block rounded-full px-2.5 py-0.5 font-mono text-[0.65rem] uppercase tracking-wide ${STATUS_STYLE[doc.status]}`}
        >
          {doc.status}
        </span>
      </div>

      <div className="flex flex-col gap-3 rounded-md border border-line bg-paper-deep/30 p-3.5">
        {doc.items.map((item, i) => (
          <div key={i} className="flex items-start justify-between gap-3 border-b border-dashed border-line pb-3 last:border-none last:pb-0">
            <div className="min-w-0">
              <p className="truncate text-sm text-ink">{item.label}</p>
              <p className="truncate text-xs text-ink-soft">{item.detail}</p>
            </div>
            <p className="shrink-0 font-mono text-sm text-ink">{item.amount}</p>
          </div>
        ))}
      </div>

      <div className="flex items-center justify-between border-t border-line pt-3">
        <span className="text-xs uppercase tracking-wide text-ink-soft">Total</span>
        <span className="font-mono text-base font-medium text-ledger-deep">{doc.total}</span>
      </div>

      <p className="text-xs leading-relaxed text-ink-soft">{doc.notes}</p>

      <p className="text-xs text-ink-soft">Issued {doc.date}</p>

      <div className="mt-1 flex gap-2">
        <button className="flex-1 rounded-md bg-ledger px-3 py-2 text-sm font-medium text-paper hover:opacity-90">
          Share in chat
        </button>
        <button className="flex-1 rounded-md border border-line px-3 py-2 text-sm text-ink hover:bg-black/[0.03]">
          Edit {kind}
        </button>
      </div>
    </div>
  );
}

function EmptyDocument({ kind }: { kind: DocKind }) {
  return (
    <div className="flex h-full flex-col items-center justify-center gap-3 text-center">
      <div className="flex h-11 w-11 items-center justify-center rounded-full border border-dashed border-line text-ink-soft">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path
            d="M12 5V19M5 12H19"
            stroke="currentColor"
            strokeWidth="1.8"
            strokeLinecap="round"
          />
        </svg>
      </div>
      <p className="max-w-[220px] text-sm text-ink-soft">
        No {kind} yet for this chat. Create one to share pricing and scope with the client.
      </p>
      <button className="rounded-md border border-line px-3.5 py-2 text-sm font-medium text-ink hover:bg-black/[0.03]">
        New {kind}
      </button>
    </div>
  );
}
