import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

client = Groq(api_key=api_key)


def generate_explanation(row):
    prompt = f"""
    Explain why this delivery job is risky in simple terms.

    Job ID: {row['job_id']}
    Delay: {row['delay']}
    Priority: {row['priority']}
    Traffic: {row['traffic_level']}
    Status: {row['status']}
    Risk Level: {row['risk_level']}

    Keep it short and clear.
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content