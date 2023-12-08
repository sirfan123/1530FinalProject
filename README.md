# CS1530 Final Project
## Product Owner: Samih Irfan
## Scrum Master: Kareem Mohsen 
## Developer(s): Danish Ghumman, Samih Irfan, Kareem Mohsen

### This is our submission for the final project

# Product Backlog

Below is the link to our Trello board for our standup meetings

[https://trello.com/b/EmCsil2r/final-project](https://trello.com/b/EmCsil2r/final-project)https://trello.com/b/EmCsil2r/final-project

# Writeup
In our development process, we utilized 3 sprints. In our Sprint 0 (on Saturday) we decided on numerous things. First, we discussed each member’s role. Kareem would be the scrum master, responsible for making sure that scrum is both understood and meetings are taking place. Samih would be the product owner, responsible for the upkeep of the product backlog, i.e. updating and curating the tasks and subtasks in our Trello kanban board. Danish would be the main software developer, in charge of technical decisions. 
Second, we also decided on a schedule for our sprints and meetings: we would do one sprint cycle per day spread across three days. Regarding the meetings of the two main sprints (Sprints 1 and 2), we had a sprint planning meeting, a daily scrum meeting, and a sprint review at the end of the sprint. Sprint 1’s review also included the planning meeting of Sprint 2. 
Last, we all contributed to the creation of the overall Product Backlog for our software, which we developed based on our functional requirements. From that backlog, we prioritized features, leading us to have our main five features that we put into our Trello board and in our final Product backlog. From those five, we decided to focus on two main features, being the implementation of Coding Challenges as well as the corresponding Learning Path that includes those coding challenges.
Sprint 1 (on Monday) involved us developing the infrastructure necessary to be able to make progress on our backlog features. This included us setting up our development and testing environments and creating the actual coding infrastructure (files, classes) needed. Sprint 2 (on Tuesday) involved us developing our two main features and their respective subtasks.

## Timeline

| Saturday | Monday  | Tuesday |
|----------------------|-------------------|--------------------|
|      Sprint 0        |      Sprint 1     |       Sprint 2     |


                                                                             

# Project Setup Guide

For first time users 

1. Clone repo into preferred IDE
2. In terminal type cd CodingChallenges
3. If python pip is not installed type following step
4. Installing pip via VS Code terminal window
    a) in the terminal window, type: py -m pip install --upgrade pip
        Important Note: some MS Windows users will get an error in the above command. 
                    One possible cause of such problem is the execution policy in  
                    your computer. To check what policy you have in your computer 
                    and change it if necessary is shown below:
        i)   Select Start > All Programs > Windows PowerShell version > Windows PowerShell.
        ii)  Type Set-ExecutionPolicy RemoteSigned to set the policy to RemoteSigned.
        iii) Type Set-ExecutionPolicy Unrestricted to set the policy to Unrestricted.
        iv)  Type Get-ExecutionPolicy to verify the current settings for the execution policy.
        v)   Type Exit.
5. Activating a virtual environment(We have already created the enviorment you simply need to run it as a user)
    a) Activating the virtual environment
       i)  In Mac OS type:   source ./bin/activate
       ii) In Windows type:  .\Scripts\activate
    Note: check if your terminal command prompt has the project name in between parenthesis
6. Intalling Flask 
    a) in the terminal window, type: pip install flask
7. Running your flask application
    a) double check that your virtual enviroment is on. If not, use step 5 
       to activate the virtual environment
    b) In the terminal window, type "python3 main.py" or "python main.py" depending on if you have python or python3
       You should see the following message in the terminal window:
       Running on http://127.0.0.1:5000/ (Press CTRL+C to open our app)
 



