import os
from git import Repo
git_dir = os.getcwd()+ "/.git"
if(os.path.exists(git_dir)):
    try:
            repo = Repo(git_dir)
            origin =repo.remote(name="origin")
            origin.push()
            print("Pushed Sucessfully!")
    except:
            print("Error occured while pushing repository to origin")