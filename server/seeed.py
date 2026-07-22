import asyncio

from uuid import uuid4
from datetime import datetime, timezone, timedelta

from app.config.session import AsyncSessionLocal

from app.models.user import User, UserRole
from app.models.meeting import (
    Meeting,
    MeetingPlatform,
    MeetingStatus,
)

from app.models.conversation import (
    Conversation,
    SpeakerRole,
    ConversationStatus,
)


async def seed_database():

    async with AsyncSessionLocal() as db:

        now = datetime.now(timezone.utc)


        # ==========================
        # USERS
        # ==========================

        users = [

            User(
                id=uuid4(),
                name="James Mwangi",
                email="james.admin@jitume.ai",
                password="hashed_password",
                role=UserRole.ADMIN,
                is_active=True,
            ),


            User(
                id=uuid4(),
                name="Peter Otieno",
                email="peter.admin@jitume.ai",
                password="hashed_password",
                role=UserRole.ADMIN,
                is_active=True,
            ),


            User(
                id=uuid4(),
                name="John Kamau",
                email="john.client@gmail.com",
                password="hashed_password",
                role=UserRole.CLIENT,
                is_active=True,
            ),


            User(
                id=uuid4(),
                name="Mary Wanjiku",
                email="mary.client@gmail.com",
                password="hashed_password",
                role=UserRole.CLIENT,
                is_active=True,
            ),

        ]


        db.add_all(users)



        # ==========================
        # MEETINGS
        # ==========================


        meeting1 = Meeting(
            id=uuid4(),
            title="AI Customer Support Platform",
            client_name="ABC Technologies",
            platform=MeetingPlatform.GOOGLE_MEET,
            meeting_date=now - timedelta(days=5),
            meeting_link="https://meet.google.com/demo1",
            fathom_meeting_id="fathom-001",
            recording_url="https://fathom.ai/demo1",
            transcript_url="https://fathom.ai/transcript1",
            status=MeetingStatus.TRANSCRIBED,
        )


        meeting2 = Meeting(
            id=uuid4(),
            title="Solar Monitoring Dashboard",
            client_name="Green Energy Ltd",
            platform=MeetingPlatform.ZOOM,
            meeting_date=now - timedelta(days=3),
            meeting_link="https://zoom.us/demo2",
            fathom_meeting_id="fathom-002",
            recording_url="https://fathom.ai/demo2",
            transcript_url="https://fathom.ai/transcript2",
            status=MeetingStatus.SUMMARIZED,
        )


        meeting3 = Meeting(
            id=uuid4(),
            title="AI Loan Risk Assessment",
            client_name="Fintech Africa",
            platform=MeetingPlatform.MICROSOFT_TEAMS,
            meeting_date=now - timedelta(days=1),
            meeting_link="https://teams.microsoft.com/demo3",
            fathom_meeting_id="fathom-003",
            recording_url="https://fathom.ai/demo3",
            transcript_url="https://fathom.ai/transcript3",
            status=MeetingStatus.RECORDING,
        )


        meeting4 = Meeting(
            id=uuid4(),
            title="Healthcare AI Assistant",
            client_name="Healthcare Solutions",
            platform=MeetingPlatform.GOOGLE_MEET,
            meeting_date=now - timedelta(hours=8),
            meeting_link="https://meet.google.com/demo4",
            fathom_meeting_id="fathom-004",
            recording_url="https://fathom.ai/demo4",
            transcript_url="https://fathom.ai/transcript4",
            status=MeetingStatus.PROPOSAL_GENERATED,
        )


        meetings = [
            meeting1,
            meeting2,
            meeting3,
            meeting4,
        ]


        db.add_all(meetings)



        # ==========================
        # CONVERSATIONS
        # ==========================


        conversations = [

            # CLIENT 1

            Conversation(
                id=uuid4(),
                meeting_id=meeting1.id,
                sequence_number=1,
                speaker=SpeakerRole.CLIENT,
                speaker_label="John Kamau",
                message="We need an AI customer support platform integrated with our CRM.",
                confidence_score=0.96,
                ai_summary="Client requires AI CRM support automation.",
                ai_entities="CRM, AI chatbot, Customer Support",
                ai_processed=True,
                status=ConversationStatus.PROCESSED,
                timestamp=now - timedelta(days=5,hours=3),
            ),


            Conversation(
                id=uuid4(),
                meeting_id=meeting1.id,
                sequence_number=2,
                speaker=SpeakerRole.ADMIN,
                speaker_label="James Mwangi",
                message="We will analyse CRM APIs and prepare an AI integration proposal.",
                confidence_score=0.98,
                ai_summary="Admin confirmed proposal preparation.",
                ai_entities="API Integration, Proposal",
                ai_processed=True,
                status=ConversationStatus.REVIEWED,
                timestamp=now - timedelta(days=5,hours=2),
            ),



            # CLIENT 2

            Conversation(
                id=uuid4(),
                meeting_id=meeting2.id,
                sequence_number=1,
                speaker=SpeakerRole.CLIENT,
                speaker_label="Mary Wanjiku",
                message="We need a dashboard to monitor solar installations.",
                confidence_score=0.94,
                ai_summary="Solar IoT monitoring requirement.",
                ai_entities="IoT, Dashboard, Solar",
                ai_processed=False,
                status=ConversationStatus.CAPTURED,
                timestamp=now - timedelta(days=3,hours=6),
            ),


            Conversation(
                id=uuid4(),
                meeting_id=meeting2.id,
                sequence_number=2,
                speaker=SpeakerRole.ADMIN,
                speaker_label="Peter Otieno",
                message="Our team will design IoT architecture and analytics.",
                confidence_score=0.97,
                ai_summary="Technical solution discussion.",
                ai_entities="IoT Architecture",
                ai_processed=True,
                status=ConversationStatus.PROCESSED,
                timestamp=now - timedelta(days=3,hours=5),
            ),



            # CLIENT 3

            Conversation(
                id=uuid4(),
                meeting_id=meeting3.id,
                sequence_number=1,
                speaker=SpeakerRole.CLIENT,
                speaker_label="David Kiptoo",
                message="We require AI loan approval and risk analysis.",
                confidence_score=0.95,
                ai_summary="Fintech AI risk assessment request.",
                ai_entities="AI Model, Loans, Risk",
                ai_processed=False,
                status=ConversationStatus.CAPTURED,
                timestamp=now - timedelta(days=1,hours=4),
            ),



            # CLIENT 4

            Conversation(
                id=uuid4(),
                meeting_id=meeting4.id,
                sequence_number=1,
                speaker=SpeakerRole.CLIENT,
                speaker_label="Anne Njeri",
                message="We need AI to summarize medical reports and meetings.",
                confidence_score=0.93,
                ai_summary="Healthcare AI assistant requirement.",
                ai_entities="Healthcare, NLP",
                ai_processed=True,
                status=ConversationStatus.PROCESSED,
                timestamp=now - timedelta(hours=8),
            ),

        ]


        db.add_all(conversations)


        await db.commit()


        print("✅ Users, Meetings and Conversations seeded successfully")



if __name__ == "__main__":
    asyncio.run(seed_database())
    