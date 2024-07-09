from crewai import Agent
from textwrap import dedent
from langchain.llms import OpenAI, Ollama
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()



# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:

    def researcher(self):
        return Agent(
    role = "Senior Research Assistant",
    goal = "Look up the latest trending website designs",
    backstory = """You work at a leading tech company.
    Your expertise lies in searcing Google for web design concepts.
    You have a knack for dissecting complex data and presenting actionable insights.""",
    verbose=True,
    allow_delegation=False,
    tool=[search_tool],
    llm= ChatOpenAI(model_name="gpt-4-turbo", temperature=0.2)
)


    def designer(self):
        return Agent(
            role = "Senior UX/UI designer",
    goal = "Design the looks and experience of the website specified in the task",
    backstory = """You work at a leading tech company.
    Your expertise lies in designing beautiful user interfaces.
    You have a knack for combining research with your own ideas to create smooth experiences.""",
    verbose=True,
    allow_delegation=True,
    llm= ChatOpenAI(model_name="dall-e-3", temperature=0.8)
)
    def developer(self):
        return Agent(
            role = "Senior Web Developer",
    goal = "Build the website with efficient and understandable code using HTML, CSS and Javascript",
    backstory = """You work at a leading tech company.
    Your expertise lies in building precisely the designs given to you.
    You have a knack for writing simple but efficient code.""",
    verbose=True,
    allow_delegation=True,
    llm= ChatOpenAI(model_name="gpt-4-turbo", temperature=0.3)
)
