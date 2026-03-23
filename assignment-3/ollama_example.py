import ollama

def query_api(prompt):
    try:
        response = ollama.chat(
            model="tinyllama",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )
        return response['message']['content']
    except Exception as e:
        return f"Error: {str(e)}"


user_input = input("Enter your prompt: ")
print(query_api(user_input))