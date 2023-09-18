import openai
import os

# Initialize OpenAI using an environment variable
openai.api_key = os.getenv("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")

def generate_content(prompt):
    try:
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=prompt,
            max_tokens=4096,
            temperature=0.7,
            top_p=0.85
        )
        generated_content = response.choices[0].text.strip()
        return generated_content
    except openai.error.OpenAIError as e:
        print(f"OpenAI API call failed: {e}")
        return "Error generating content. Please try again later."

