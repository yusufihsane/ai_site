from groq import Groq

client = Groq(api_key="kendi groq apin")

def cevap_ver(mesaj):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": mesaj}]
    )

    return response.choices[0].message.content