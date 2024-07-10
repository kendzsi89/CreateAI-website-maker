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
            description="""Using the insights provided, pick two or three design elements from them that you'll use to showcase in your designs. 
            Then develop a set of 3 images that showcases your UX design, using prompts that work well with Dall-e 3.
            The images should include branding, identity and page layouts.""",
        expected_output="3 website design images, 1 branding identity guideline",
        agent=agent
        )
    
    def task3(self, agent):
        return Task(
    description="""Using the design images provided, build a functioning website using HTML, CSS and Javascript that is precisely like the images.
     Add comments in your code for clarity. Take care about responsiveness over mobile and desktop.""",
    expected_output="three files: index.html, styles.css, script.js",
    agent=agent
)
