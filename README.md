# Connected_LLM
A simple LLM connection
In this repository you can find everything you need to connect to ChatGPT API and how to use python properly.
## Python and Virtual Environment 

Most of the issues you have been dealing with is about the wrong usage of the python, first of all almost any python project should contain a virtual environemnt to avoid version problems. 

### Waht is Virtual Environment? 

A virtual environment is like a self-contained copy of the Python interpreter along with its standard library. It allows you to create an isolated environment for your Python project, ensuring that the dependencies for one project don't interfere with those of another.

### Why We Need Virtual Environment ? 

- Isolation: Keeps project dependincies out of systems and computers, while using venv we use the venv python interpreter for running our scripts. 
- Version Management: Sometimes we use old versions of the libraries, or we can use differetn variables. Venv helps us to use the correct and saved versions.  

These are the main advantages of Python Virtual Environement. 

### How to create a Venv? 

Open your project directory in your terminal, remember you need Python installed on your PC. While you are into the project directory;

- python3 -m venv myvenv // For linux 

This terminal command will create your venv now lets activate the venv 

- source myenv/bin/activate

And this command will activate your venv, now you will use this environment to run your scripts and add libraries. 


## How to connect OpenAI API 

- First of all you need to create an API key from: https://platform.openai.com/docs/guides/text-generation 
- Then everything is very simple, while your venv active run this command to add OpenAI library to your project 

    . pip install --upgrade openai

This command will install and upgrade to the latest version of the library of OpenAI into your venv. 

Now open a main file and lets connect to the GPT-3.5, go and examine the main.py, you can dirctly clone that repository. If there is anything you want to ask just create an issue and let me check... 



