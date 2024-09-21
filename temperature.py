import os
import sys
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env file
load_dotenv()

def get_text_response(input_content, temperature):
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # You may want to adjust this to the appropriate OpenAI model
        messages=[
            {
                "role": "user",
                "content": input_content
            }
        ],
        max_tokens=2000,
        temperature=temperature,
        top_p=0.9,
        stop=None
    )

    return response.choices[0].message.content

# Main execution
if __name__ == "__main__":
    for i in range(3):
        response = get_text_response(sys.argv[1], float(sys.argv[2]))
        print(response, end='\n\n')