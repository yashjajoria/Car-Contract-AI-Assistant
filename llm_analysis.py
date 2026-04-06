import ollama


def analyze_with_llm(contract_text):

    prompt = f"""
You are a legal assistant.

Analyze the following car lease agreement and extract:

1. Short summary
2. Lease duration
3. Monthly payment
4. Vehicle VIN
5. Risky clauses
6. Negotiation suggestions

Agreement text:
{contract_text}
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"]

    except Exception as e:

        return f"""
LLM Error

Ollama is not running or model not found.

Possible fixes:
1. Run: ollama serve
2. Run: ollama pull llama3
3. Restart Streamlit

Error details:
{e}
"""