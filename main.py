from dotenv import load_dotenv
load_dotenv()
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI


from textwrap import dedent
from agents import CustomAgents
from tasks import CustomTasks


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        custom_agent_1 = agents.researcher()
        custom_agent_2 = agents.designer()
        custom_agent_3 = agents.developer()

        # Custom tasks include agent name and variables as input
        custom_task_1 = tasks.task1(
            custom_agent_1,
        )

        custom_task_2 = tasks.task2(
            custom_agent_2,
        )

        custom_task_3 = tasks.task3(
            custom_agent_3,
        )

        # Define your custom crew here
        crew = Crew(
            agents=[custom_agent_1, custom_agent_2, custom_agent_3],
            tasks=[custom_task_1, custom_task_2, custom_task_3],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Template")
    print("-------------------------------")


    custom_crew = CustomCrew()
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
