import json
from ApiInteractionCrew import ApiInteractionCrew
from crewai import Crew
import os
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env

# Read your API key from the environment variable
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
#print("\n--- gemini_api_key:", GOOGLE_API_KEY)


# Use Gemini 1.5 Pro or other Gemini models
# Note the format: 'gemini/model-name'
gemini_llm = LLM(
    model='gemini/gemini-2.5-flash-preview-05-20',  # Or 'gemini/gemini-1.5-flash', etc.
    api_key=GOOGLE_API_KEY,
    temperature=0.7,  # Adjust temperature for creativity (0.0 to 1.0)
    # Add other parameters as needed, e.g., max_tokens, top_p, etc.
)

def run():
    method = input("Enter HTTP method (GET, POST, PUT): ").strip().upper()
    url = input("Enter the API URL: ").strip()

    data = {}
    if method in ["POST", "PUT"]:
        json_input = input("Enter JSON request data: ").strip()
        try:
            data = json.loads(json_input)
        except json.JSONDecodeError:
            print("Invalid JSON format. Exiting.")
            return

    inputs = {
        "method": method,
        "url": url,
        "data": data
    }

    crew_factory = ApiInteractionCrew(inputs)
    agent = crew_factory.simple_api_agent(gemini_llm)

    task_description = ""
    expected_output_description = ""
    if method == "GET":
        task_description = f"Perform a GET request to the URL: {url}. Use the 'REST API Tool' with method='GET' and url='{url}'."
        expected_output_description = "The JSON response from the GET request."
    elif method == "POST":
        task_description = f"Perform a POST request to the URL: {url} with the following JSON data: {json.dumps(data)}. Use the 'REST API Tool' with method='POST', url='{url}', and data={json.dumps(data)}."
        expected_output_description = "The JSON response from the POST request."
    elif method == "PUT":
        task_description = f"Perform a PUT request to the URL: {url} with the following JSON data: {json.dumps(data)}. Use the 'REST API Tool' with method='PUT', url='{url}', and data={json.dumps(data)}."
        expected_output_description = "The JSON response from the PUT request."

    if not task_description:
        task = None # Ensure task is None if method is unsupported
    else:
        task = Task(
            description=task_description,
            agent=agent,
            expected_output=expected_output_description
        )

    if task is None: # Check if task was successfully created
        print(f"Unsupported method '{method}'. Exiting.")
        return

    crew = Crew(
        agents=[agent],
        tasks=[task],
        verbose=True
    )
    crew.kickoff(inputs=inputs)

if __name__ == "__main__":
    run()