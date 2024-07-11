from crewai import Task
from openai import OpenAI


# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def __tip_section(self):
        return "If you do your BEST WORK, I'll give you a $10,000 commission!"
    

    def task1(self, agent):
        return Task(
            description="""Conduct a comprehensive analysis of the latest trends in web design in July 2024.
    Identify new and brave ideas, new technologies, and potential industry impacts.""",
            expected_output="Full analysis report in bullet points",
            
            agent=agent
        )

    def task2(self, agent, imageGeneration):
        return Task(
            description="""Using the insights provided, pick two or three design elements from them that you'll use to showcase in your website design. 
            Then develop a set of 3 prompts for Dall-e to create your designs for a 3-page website.
            One of the pages should be the Homepage or landing page. The other two are up to you.
            The images should include branding, identity and page layouts, and they should be cohesive and work as one website.""",
        expected_output="""an API call with 3 prompts for 3 website design images, 1 branding identity guideline.
        
        Example output:
        [
        "a beautiful landing page with an animated toroid in the background, with sans serif hero title, dark blue, silver, light mode",
        "an interactive contact section with zooming hover effects, dark blue, silver, light mode",
        "an animated game showcasing a leading developer portfolio, dark blue, silver, light mode",
        ]
        """,
        agent=agent,
        callback=imageGeneration
        )
    
    def task3(self, agent, image_links):
        return Task(
    description="""Using the three images {image_links} provided, go through the following steps:
    1. Analyze precisely what you see in the images. As context, these are website pages with various elements in different positions in the images. Per image, list every element you can identify, specify their positions and sizes, and even go into detail about colours. be as precise as you can be, and don't leave out anything. 
    2. Think which elements have to be separate or grouped together to make an efficient but useful React DOM. Generate react component code blocks and a single css block, using your own precise explanations of the images.
    3. Take care about responsiveness over mobile and desktop.
    4. After you're done generating the react and css contents, create an index.js and import all of the react components into a single DOM with Navigation
    """,
    expected_output=""" an object containing a set of jsx components, one index.js and one styles.css.
    Example output: 
    {
    index.html: `<html lang="en">
  <head>
    <meta charset="utf-8" />
    <link rel="icon" href="%PUBLIC_URL%/favicon.ico" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <meta name="theme-color" content="#000000" />
    <meta
      name="description"
      content="Web site created using create-react-app"
    />
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
    />
    <title>React App</title>
  </head>
  <body>
    <noscript>You need to enable JavaScript to run this app.</noscript>
    <div id="root"></div>
  </body>
</html>`,
    styles.css: `body {
  margin: 0;
  font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", "Oxygen",
    "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue",
    sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

code {
  font-family: source-code-pro, Menlo, Monaco, Consolas, "Courier New",
    monospace;
}
a {
  text-decoration: none;
  color: black;
}
a:hover {
  text-decoration: none;
  color: rgba(0, 0, 0, 0.349);
}
`,
about.jsx: `import React from "react";

function About() {
  return (
    <div className="about">
      <div class="container">
        <div class="row align-items-center my-5">
          <div class="col-lg-7">
            <img
              class="img-fluid rounded mb-4 mb-lg-0"
              src="http://placehold.it/900x400"
              alt=""
            />
          </div>
          <div class="col-lg-5">
            <h1 class="font-weight-light">About</h1>
            <p>
              Lorem Ipsum is simply dummy text of the printing and typesetting
              industry. Lorem Ipsum has been the industry's standard dummy text
              ever since the 1500s, when an unknown printer took a galley of
              type and scrambled it to make a type specimen book.
            </p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default About;
`,
 ...MORE JSX COMPONENTS...
 
index.js: `import React from "react";
import ReactDOM from "react-dom";
import "./index.css";
import * as serviceWorker from "./serviceWorker";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import {
  Navigation,
  Footer,
  Home,
  About,
  Contact,
  Blog,
  Posts,
  Post,
} from "./components";

ReactDOM.render(
  <Router>
    <Navigation />
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/about" element={<About />} />
      <Route path="/contact" element={<Contact />} />
      <Route path="/blog" element={<Blog />}>
        <Route path="" element={<Posts />} />
        <Route path=":postSlug" element={<Post />} />
      </Route>
    </Routes>
    <Footer />
  </Router>,

  document.getElementById("root")
);

serviceWorker.unregister();
`,        """,
    agent=agent
)
