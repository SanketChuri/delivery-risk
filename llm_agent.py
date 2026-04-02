from groq import Groq

client = Groq(api_key="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")


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