from typing import ClassVar, Dict, Any
import requests
import json
from crewai.tools import BaseTool

class HttpAgentTool(BaseTool):
   
    inputs: ClassVar[Dict[str, Any]] = {'method': '', 'url': '', 'data': {}}
    def __init__(self,input_data):
        super().__init__()
        HttpAgentTool.inputs = input_data        
        print("self.input_data",self.inputs)       
        
    
    name: str = "REST API Tool" # The name of the tool
    description: str = "A tool for executing REST API requests (GET, POST, PUT). Expects 'method' (string, e.g., 'GET', 'POST', 'PUT'), 'url' (string), and optionally 'data' (dictionary for POST/PUT)."
   
    
    def _run(self):
        method = HttpAgentTool.inputs.get("method")
        url = HttpAgentTool.inputs.get("url")
        data = HttpAgentTool.inputs.get("data", {})
        headers = {"Content-Type": "application/json"}

        try:
            method = method.upper()
            if method == "POST":
                response = requests.post(url, json=data, headers=headers)
            elif method == "PUT":
                response = requests.put(url, json=data, headers=headers)
            elif method == "GET":
                response = requests.get(url, headers=headers)
            else:
                return {"error": f"Unsupported method: {method}"}
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return f"Error during request to {url}: {e}"
        except json.JSONDecodeError:
            return f"Failed to decode JSON from response. Text: {response.text}"