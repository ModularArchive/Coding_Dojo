Assignment: Practice your pip in your virtual environment
Objectives:
Get accustomed to using commands required to use pip modules
Practice using a virtual environment
You will need to use your terminal to run these commands. Open up terminal, command prompt, or git bash to continue. Activate your virtual environment before running any of these commands! Remember that you can tell whether your virtual environment is activated by the prompt in your terminal. Here, we can see that the virtual environment py3Env is activated:



 Run these commands in the order instructed. Your assignment submission should be a .txt file that includes a short explanation of what you were able to learn about each command by doing a brief (1-2 min) web search for each term. If it is relevant, include the output of your command and your understanding of what it means. It is important to always read your terminal output and try to understand it.

Reminder: when your virtualenv is activated, you may use the pip command. If not, use pip3.

Run the following commands:

pip install Django==1.11.9

pip list

deactivate (This will deactivate your virtual environment)

pip3 list (How is the result different from when you ran pip list with the virtualenv activated? Hint, you should not have as many things listed when the virtualenv is deactivated. If your results are the same, go back and figure out what went wrong.)

source myEnvironments/py3Env/bin/activate (Adjust the path as needed to re-activate the virtualenv; for windows call myEnvironments/py3Env/Scripts/activate)

pip install Django==1.11.9 (We know you already ran this one. What information do you see returned in terminal after this command?)

pip freeze (What's the difference between freeze and list?)

First cd into your Desktop directory (cd ~/Desktop), then run this command: pip freeze > requirements.txt. What do you see when you ls? What's inside this file?

pip uninstall Django

pip show Django

pip search Flask This one might take a moment to execute.