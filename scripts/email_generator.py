from openai import OpenAI

client = OpenAI()

def generate_email(topic):
    response = client.responses.create(
        model="gpt-4.1-mini",
        input=f"Write a professional email about: {topic}"
    )
    return response.output_text

if __name__ == "__main__":
    topic = input("Email topic: ")
    email = generate_email(topic)

    print("\nGenerated Email:\n")
    print(email)
