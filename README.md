# simple-crewai-restapi
This repo shows the integration of Crewai Framework for calling REST API using Google Gemini LLM Simple CrewAI REST API A simple and lightweight RESTful API built with FastAPI that exposes the functionalities of CrewAI, allowing you to integrate powerful agent-based workflows into your applications via HTTP requests.
Here's a `README.md` file for the repository: [https://github.com/shdhumale/simple-crewai-restapi.git](https://github.com/shdhumale/simple-crewai-restapi.git), which appears to demonstrate integrating **CrewAI agents** with a **REST API** using Python.

---

````markdown
# Simple CrewAI REST API

This repository demonstrates a simple implementation of the [CrewAI](https://github.com/CrewAI-Inc/crewAI) framework where autonomous agents collaborate to process user input and interact with an external RESTful API.

## 🚀 Project Overview

The goal of this project is to show how CrewAI agents can:

- Receive a user input query
- Extract keywords or intents
- Make a call to a public REST API
- Return a structured response back to the user

The example uses a fictional or demo REST endpoint to retrieve object data based on a predefined ID.

---

## 📂 Project Structure

```bash
simple-crewai-restapi/
│
├── main.py                 # Main entry point to run the Crew and agents
├── agents/
│   └── agent_config.py     # Defines agents and their responsibilities
├── tools/
│   └── api_tool.py         # Tool to call the REST API using requests
├── .env                    # Stores API keys or environment configs
├── requirements.txt        # List of Python dependencies
└── README.md               # Project documentation
````

---

## 🧠 How It Works

1. **Agents** are defined with specific roles (e.g., `ResearcherAgent`, `ApiCallerAgent`).
2. A REST API tool is registered to allow agents to call `https://api.restful-api.dev/objects/7`.
3. The `main.py` script sets up the Crew, agents, tools, and runs the workflow.
4. Final output is generated based on the agent collaboration and API response.

---

## 🔧 Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/shdhumale/simple-crewai-restapi.git
cd simple-crewai-restapi
```

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Environment Variables

Create a `.env` file and add any required keys or variables (if needed). For this example, no external API keys are used.

### 5. Run the Application

```bash
python main.py
```

---

## 📡 Example Output

```
Crew started working...
Agent [ResearcherAgent] received the task.
Calling REST API: https://api.restful-api.dev/objects/7
API Response: {
  "name": "Apple MacBook Pro 16",
  "data": {
    "year": 2019,
    "price": "$2399",
    ...
  }
}
Crew finished. Final output generated.
```

---

## 📦 Dependencies

* Python 3.9+
* [CrewAI](https://github.com/CrewAI-Inc/crewAI)
* `requests`
* `python-dotenv`

---

## 🤝 Contributing

Pull requests are welcome! If you find a bug or have suggestions to improve this example, feel free to open an issue or submit a PR.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Siddharatha Dhumale**
[GitHub Profile](https://github.com/shdhumale)

---

## 📬 Contact

For questions or collaborations, feel free to connect via GitHub.

```

Let me know if you’d like a Hindi version or want this tailored for a blog post or video explanation.
```
