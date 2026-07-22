import { ChatRecord } from './types';

export const currentUser = {
  name: 'Amara Osei',
  role: 'Account Manager',
  initials: 'AO',
};

export const chats: ChatRecord[] = [
  {
    id: 'c1',
    name: 'Daniel Mwangi',
    company: 'Highline Freight Co.',
    lastMessage: 'Can you send the updated quotation?',
    lastTime: '09:42',
    unread: 2,
    messages: [
      { id: 'm1', author: 'them', text: 'Morning! We reviewed the draft scope.', time: '09:12' },
      { id: 'm2', author: 'them', text: 'A few line items need adjusting before we sign off.', time: '09:13' },
      { id: 'm3', author: 'me', text: 'Sure — which ones stand out to you?', time: '09:20' },
      { id: 'm4', author: 'them', text: 'Mostly the freight handling and the warehousing tier.', time: '09:35' },
      { id: 'm5', author: 'them', text: 'Can you send the updated quotation?', time: '09:42' },
    ],
    documents: {
      quotation: {
        reference: 'QT-2026-0143',
        title: 'Regional Freight Handling — Q3',
        status: 'sent',
        date: 'Jul 18, 2026',
        items: [
          { label: 'Freight handling', detail: 'Per-pallet, regional routes', amount: 'KSh 84,000' },
          { label: 'Warehousing', detail: 'Tier 2, 30-day cycle', amount: 'KSh 46,500' },
          { label: 'Customs coordination', detail: 'Flat rate', amount: 'KSh 12,000' },
        ],
        total: 'KSh 142,500',
        notes: 'Rates hold for 14 days from issue date.',
      },
      proposal: null,
    },
  },
  {
    id: 'c2',
    name: 'Wanjiru Kamau',
    company: 'Baraka Retail Group',
    lastMessage: 'Proposal looks solid, sending to finance.',
    lastTime: 'Yesterday',
    unread: 0,
    messages: [
      { id: 'm1', author: 'me', text: 'Attached is the revised proposal for the loyalty rollout.', time: '16:02' },
      { id: 'm2', author: 'them', text: 'Thanks — structure reads much clearer now.', time: '16:40' },
      { id: 'm3', author: 'them', text: 'Proposal looks solid, sending to finance.', time: '17:05' },
    ],
    documents: {
      proposal: {
        reference: 'PR-2026-0071',
        title: 'Loyalty Programme Rollout',
        status: 'accepted',
        date: 'Jul 20, 2026',
        items: [
          { label: 'Discovery & mapping', detail: '2 weeks, in-store audit', amount: 'KSh 60,000' },
          { label: 'Platform build', detail: 'Points engine + tiering', amount: 'KSh 210,000' },
          { label: 'Staff onboarding', detail: '4 branches', amount: 'KSh 28,000' },
        ],
        total: 'KSh 298,000',
        notes: 'Phase two (analytics dashboard) to be scoped separately.',
      },
      quotation: null,
    },
  },
  {
    id: 'c3',
    name: 'Peter Otieno',
    company: 'Rift Valley Agrotech',
    lastMessage: 'Could we get both a proposal and a quotation?',
    lastTime: 'Mon',
    unread: 1,
    messages: [
      { id: 'm1', author: 'them', text: 'We are comparing two paths for the irrigation upgrade.', time: '11:00' },
      { id: 'm2', author: 'them', text: 'Could we get both a proposal and a quotation?', time: '11:04' },
      { id: 'm3', author: 'me', text: 'Yes, I will prepare both for comparison.', time: '11:20' },
    ],
    documents: {
      proposal: {
        reference: 'PR-2026-0088',
        title: 'Drip Irrigation Upgrade — Full Scope',
        status: 'draft',
        date: 'Jul 21, 2026',
        items: [
          { label: 'Site survey', detail: '3 plots', amount: 'KSh 18,000' },
          { label: 'System design', detail: 'Drip + sensor network', amount: 'KSh 95,000' },
          { label: 'Installation', detail: 'Labour + materials', amount: 'KSh 220,000' },
        ],
        total: 'KSh 333,000',
        notes: 'Includes 12-month sensor monitoring subscription.',
      },
      quotation: {
        reference: 'QT-2026-0156',
        title: 'Drip Irrigation — Materials Only',
        status: 'draft',
        date: 'Jul 21, 2026',
        items: [
          { label: 'Drip lines & emitters', detail: '3 plots', amount: 'KSh 140,000' },
          { label: 'Sensor units', detail: 'x6 units', amount: 'KSh 54,000' },
        ],
        total: 'KSh 194,000',
        notes: 'Installation labour billed separately if selected.',
      },
    },
  },
  {
    id: 'c4',
    name: 'Grace Nyambura',
    company: 'Coastal Textiles Ltd.',
    lastMessage: 'Thank you, we will review internally.',
    lastTime: 'Mon',
    unread: 0,
    messages: [
      { id: 'm1', author: 'me', text: 'Sharing the initial proposal for the dye-line expansion.', time: '10:00' },
      { id: 'm2', author: 'them', text: 'Thank you, we will review internally.', time: '10:45' },
    ],
    documents: { proposal: null, quotation: null },
  },
  {
    id: 'c5',
    name: 'Samuel Kiptoo',
    company: 'Nakuru Builders Ltd.',
    lastMessage: 'Send over the quotation when ready.',
    lastTime: 'Last week',
    unread: 0,
    messages: [
      { id: 'm1', author: 'them', text: 'We are ready to move on the second phase.', time: '14:00' },
      { id: 'm2', author: 'them', text: 'Send over the quotation when ready.', time: '14:02' },
    ],
    documents: { proposal: null, quotation: null },
  },
];
