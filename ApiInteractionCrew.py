from crewai import Agent, Crew, Task, Process
from crewai.project import CrewBase, agent, task, crew
from HttpAgentTool import HttpAgentTool

@CrewBase
class ApiInteractionCrew:
    def __init__(self, input_data):
        self.input_data = input_data       
    @agent
    def simple_api_agent(self, gemini_llm) -> Agent:
        return Agent(
            config=self.agents_config['simple_api_agent'],
            tools=[HttpAgentTool(self.input_data)],
            llm=gemini_llm,
            verbose=True,
        )

    @task
    def http_get_task(self, agent: Agent) -> Task:
        return Task(
            config=self.tasks_config['http_get_task'],
            agent=agent
        )

    @task
    def http_post_task(self, agent: Agent) -> Task:
        return Task(
            config=self.tasks_config['http_post_task'],
            agent=agent
        )

    @task
    def http_put_task(self, agent: Agent) -> Task:
        return Task(
            config=self.tasks_config['http_put_task'],
            agent=agent
        )