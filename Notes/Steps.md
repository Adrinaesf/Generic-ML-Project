====================================================
Starting a New Machine Learning Project (Complete Workflow)
====================================================

* Outline: 
    - Making an environment
    - Maiking a github repository

1. Making an environment
    - 1.1: Create a project folder
        ``mkdir Generic-ML-Project``
    - 1.2: Move into it:
        ``cd Generic-ML-Project``
    - 1.3: Open nit in VScode:
        ``code .``
    - 1.4: Create a Conda environment
        ``conda create -p ./venv python=3.11 -y``  
        Functionality of -p: Put the environment at this path (./venv). 
        Functionality of -y: Automatically answer yes. 
    - 1.5: Activate the environment:
        ``conda activate ./venv``
    - 1.6: Check Python: 
        ``python --version``

2. Making a repository:
    - 2.1: Got to github and make a new repository for your project. 
    - 2.2: Copy the HTTPS of project
    - 2.3: Initilize the git in terminal of VSCode
        ``git init``
        This tells git to start tracking this project.

    - 2.4: Connect the github
        ``git remote add origin https://github.com/username/project.git``

        This adds a remote named "origin": It's like my online copy of the project.
        It cfan be checked by: ``git remote -v``

    - 2.5: Create .gitignore
        Make a file called: ``.gitignore`` and write ``venv/`` in the file. 

        Why? Because venv is systemp dependent and you may have python 3.6 but it won't work on other systems if they differ, so the best practice is to make the requirment.txt. 

    - 2.6: Check the status of git 
        ``git status``

        This answers: What's changed? What hasn't? What's staged? What's untracked? Think of it as Git's dashboard.
    
    - 2.7: Add the files 
        `` git add . ``
    - 2.8: Commit
        `` git commit -m "message" ``
    - 2.9: Push
        first time: ``git push -u origin main ``
        after: ``git push``






