from twilio.rest import Client
from backend.config import *


def send_emergency_alert():
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        client.messages.create(
            body="🚨 Emergency! User may need help immediately.",
            from_=TWILIO_PHONE_NUMBER,
            to=USER_PHONE_NUMBER
        )

        return "✅ Emergency SMS sent!"
    except Exception as e:
        return f"❌ SMS Failed: {e}"


def make_emergency_call():
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

        call = client.calls.create(
            twiml="""
                <Response>
                    <Say voice="alice">
                        This is an emergency alert. The user may need immediate help.
                        Please contact them as soon as possible.
                    </Say>
                    <Pause length="1"/>
                    <Say voice="alice">
                        This is an emergency. Please respond immediately.
                    </Say>
                </Response>
            """,
            from_=TWILIO_PHONE_NUMBER,
            to=USER_PHONE_NUMBER
        )

        return "📞 Emergency call initiated!"
    except Exception as e:
        return f"❌ Call Failed: {e}"


def get_emergency_contacts(location="India"):
    return f"""
🚨 **Emergency Support Contacts ({location})**

🧠 Therapists:
- Dr. Ishita Bhatt — +91 9876543210
- Dr. Kush Singh — +91 9123456780
- MindCare Counseling Center — +91 9988776655

📞 Helplines:
- AASRA (24x7): +91-22-27546669
- Kiran Mental Health Helpline: 1800-599-0019

⚠️ If you are in immediate danger, please call emergency services.
"""