!pip install transformers

from transformers import pipeline

# Carregar o modelo para resolver problemas do tipo WSC
wsc_model = pipeline("text2text-generation", model="facebook/bart-large")

# Definir um exemplo de problema WSC
wsc_problem = {
    "text": "The trophy doesn't fit into the brown suitcase because it's too large.",
    "question": "What is too large?",
    "options": ["the trophy", "the suitcase"]
}

# Resolver o problema
result = wsc_model(
    f"resolve: {wsc_problem['text']} question: {wsc_problem['question']}",
    max_length=50
)

print("Problema WSC:")
print(wsc_problem['text'])
print("\nPergunta:")
print(wsc_problem['question'])
print("\nOpções:")
print(wsc_problem['options'])
print("\nResposta do modelo:")
print(result[0]['generated_text'])

