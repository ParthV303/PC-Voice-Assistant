from groq import Groq
from personality import PERSONALITY

client = Groq(api_key="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")

def ask_ai(prompt):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": PERSONALITY},
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content