export interface BaseResponse {
  id: string
  created_date: string
  is_active: boolean
  updated_at?: Date
}

export interface UserResponse {
    id: string
    name: string
}

export interface ChatBrief {
    id: string
    name: string
    company: string
    last_message: string
    last_time: string
    unread: number
}

export interface ChatBriefState {
    briefsLoading: boolean
    briefsError: string | null
    briefs: ChatBrief[] | null
}

export interface Message {
  id: string;
  author: 'ai' | 'me';
  text: string;
  time: string;
}

export type DocKind = 'proposal' | 'quotation';

export interface DocLineItem {
  label: string;
  detail: string;
  amount: string;
}

export interface DocumentRecord {
  reference: string;
  title: string;
  status: 'draft' | 'sent' | 'accepted';
  date: string;
  items: DocLineItem[];
  total: string;
  notes: string;
}

export interface ChatRecord extends ChatBrief {
  messages: Message[];
  documents: Record<DocKind, DocumentRecord | null>;
}