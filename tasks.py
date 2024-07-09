from crewai import Task

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"

    def task1(self, agent):
        return Task(
            description="""Conduct a comprehensive analysis of the latest trends in web design for artists in July 2024.
    Identify new and brave ideas, new technologies, and potential industry impacts.""",
            expected_output="Full analysis report in bullet points",
            
            agent=agent
        )

    def task2(self, agent):
        return Task(
            description="""Using the insights provided together with your own brilliant ideas, develop a set of 5 images that showcases your UX design.
     Include branding, identity and page layouts on mobile and desktop.""",
        expected_output="5 website design images, 1 branding identity guidelines",
        agent=agent
        )
    
    def task3(self, agent):
        return Task(
    description="""Using the design provided, build a functioning website using HTML, CSS and Javascript.
     Add comments for clarity, and test the code for bugs. Take care about responsiveness over mobile and desktop.""",
    expected_output="three files: index.html, styles.css, script.js",
    agent=agent
)
