import openai

openai.api_key = 'sk-'

def soru_cevapla(soru):
    try:
        # OpenAI'ya soruyu gönder
        cevap = openai.Completion.create(
            engine="text-davinci-003",  # GPT-4 modeli
            prompt=soru,
            max_tokens=150  # Cevabın maksimum uzunluğu
        )

        # OpenAI'den gelen cevabı al
        cevap_metni = cevap['choices'][0]['text'].strip()
        return cevap_metni
    except Exception as e:
        return str(e)

# Soru gönder ve cevabı al
response = soru_cevapla("What is the capital of Turkey?")

# Cevabı ekrana yazdır
print(response)
