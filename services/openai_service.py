import openai

def explain_music_by_ai(api_key, lyrics):
    base_url = "https://api.aimlapi.com"

    prompt =  f"Resuma de maneira breve em português a seguinte letra de musica. Texto: '{lyrics}'"

    client = openai.OpenAI(
        api_key=api_key,
        base_url=base_url
    )

    model_name = "gpt-3.5-turbo"

    chat_completion = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=256
    )

 

    response = chat_completion.choices[0].message.content
    print(f"Resposta do Modelo: {response}")