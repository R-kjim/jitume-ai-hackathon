"# jitume-ai-hackathon" 

Jitume AI Hackathon 2026 — AI Client Success Agent
<div align="center">
 Jitume AI
AI-Powered Client Success Agent for Creative Agencies

Transforming client meetings into actionable proposals, quotations, and project plans in minutes.

Built for the Jitume AI Hackathon 2026


</div>
📌 Overview

Creative agencies lose valuable time on repetitive administrative tasks after every client meeting.

Teams manually:

Listen to meeting recordings
Write meeting minutes
Create project briefs
Prepare proposals
Generate quotations
Update CRM systems
Send follow-up emails

These repetitive workflows slow project delivery, reduce productivity, and limit business growth.

Jitume AI automates this entire process using intelligent AI agents.

From a single meeting recording, the platform automatically generates:

🎤 Speech-to-text transcription
📝 Meeting summary
📋 Project brief
📑 Professional proposal
💰 Project quotation
📧 Client follow-up
📊 CRM updates
🚀 Problem Statement

Creative agencies spend hours performing repetitive administrative work after every client engagement.

Common pain points include:

Manual note taking
Slow proposal generation
Delayed quotations
Poor client follow-up
Scattered documentation
Lost project requirements
Inconsistent communication

This leads to:

Increased operational costs
Reduced productivity
Poor customer experience
Lost business opportunities
💡 Solution

Jitume AI introduces an intelligent AI Client Success Agent that automates the complete post-meeting workflow.

Instead of spending several hours preparing project documentation, users simply upload:

Meeting audio
Meeting transcript

The AI handles the rest.

✨ Features
🎙 Speech-to-Text
Upload meeting audio
Automatic transcription
Speaker identification (future)
🧠 AI Meeting Summary

Generates:

Key discussion points
Decisions made
Action items
Risks
Deadlines
📋 Project Brief Generator

Creates:

Objectives
Scope
Deliverables
Timeline
Requirements
📄 Proposal Generator

Produces professional client proposals including:

Executive Summary
Scope of Work
Timeline
Deliverables
Pricing
Terms & Conditions
💰 Quotation Generator

Automatically estimates:

Resources
Cost
Taxes
Total amount
📧 Client Follow-up

Automatically drafts:

Thank-you email
Next steps
Meeting recap
📂 CRM Update

Stores:

Client profile
Meeting history
Proposal
Project status
🏗 AI Agent Workflow
Client Meeting
        │
        ▼
Audio Upload
        │
        ▼
Speech-to-Text Agent
        │
        ▼
Transcript
        │
        ▼
Meeting Intelligence Agent
        │
        ▼
Meeting Summary
        │
        ▼
Project Brief Agent
        │
        ▼
Proposal Agent
        │
        ▼
Quotation Agent
        │
        ▼
CRM Agent
        │
        ▼
PDF Export
🏛 System Architecture
                 Next.js Frontend
                        │
                        │ REST API
                        ▼
                Python FastAPI Backend
                        │
 ┌──────────────────────┼─────────────────────┐
 │                      │                     │
 ▼                      ▼                     ▼
Whisper STT      OpenAI LLM           PostgreSQL
 │                      │                     │
 ▼                      ▼                     ▼
Transcript       AI Agents           Client Records
                        │
                        ▼
                 PDF Generator
🧠 AI Agents
🎤 Speech-to-Text Agent

Responsible for:

Audio transcription
Transcript generation
📝 Meeting Intelligence Agent

Responsible for:

Summaries
Action items
Decisions
Risks
📋 Project Brief Agent

Responsible for:

Requirements
Deliverables
Scope
Timeline
📄 Proposal Agent

Responsible for:

Proposal generation
Pricing suggestions
Project overview
💰 Quotation Agent

Responsible for:

Cost estimation
Budget
Pricing
👥 CRM Agent

Responsible for:

Client records
Meeting history
Proposal storage
🛠 Tech Stack
Frontend
Next.js 15
TypeScript
Tailwind CSS
shadcn/ui
React Hook Form
TanStack Query
Backend
Python
FastAPI
SQLAlchemy
Pydantic
Celery (Future)
AI
OpenAI GPT
Whisper
LangChain
Pydantic AI (optional)
Database
PostgreSQL
Storage
Cloudinary / AWS S3
Authentication
JWT
OAuth (Future)
PDF
ReportLab
Deployment
Docker
Docker Compose
Nginx
Vercel
Render
📂 Project Structure
jitume-ai/
│
├── ai-workflow-app/
├── app/
│   ├── globals.css
│   ├── layout.tsx
│   └── page.tsx
├── components/
│   ├── ChatView.tsx
│   └── Sidebar.tsx
├── types/
│   └── index.ts
├── package.json
├── postcss.config.mjs
└── tsconfig.json
│
├── backend/
│   ├── app/
│   │   ├── agents/
│   │   ├── api/
│   │   ├── services/
│   │   ├── models/
│   │   ├── prompts/
│   │   ├── schemas/
│   │   ├── database/
│   │   └── utils/
│   │
│   ├── uploads/
│   ├── generated/
│   └── tests/
│
├── docker/
├── docs/
└── README.md
⚙ Installation
Clone
git clone git@github.com:R-kjim/jitume-ai-hackathon.git

cd jitume-ai
Backend
cd backend

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt

uvicorn app.main:app --reload
Frontend
cd frontend

npm install

npm run dev
📸 MVP Workflow
Create Client
      │
      ▼
Upload Meeting Audio
      │
      ▼
Generate Transcript
      │
      ▼
Generate Summary
      │
      ▼
Generate Project Brief
      │
      ▼
Generate Proposal
      │
      ▼
Generate Quotation
      │
      ▼
Download PDF
🎯 Business Impact

✅ Reduces proposal preparation time by over 90%.

✅ Improves client response times.

✅ Standardizes documentation.

✅ Eliminates repetitive administrative work.

✅ Enables creative teams to focus on innovation rather than paperwork.

🚀 Future Enhancements
Multi-agent collaboration
Voice assistant
Real-time meeting transcription
Slack and Microsoft Teams integration
Google Meet & Zoom integration
CRM integrations (HubSpot, Salesforce)
Automated invoicing
Resource allocation recommendations
Analytics dashboard
Multilingual support
👨‍💻 Team

Jitume AI Hackathon 2026

Building the future of AI-powered creative agency operations.