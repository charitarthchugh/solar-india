import os
from git import Repo
import jovian
git_dir = os.getcwd()+ "/.git"
if(os.path.exists(git_dir)):
    jovian.commit(
        environment="conda",
        project="solar-india",
        filename="solar-india.ipynb",
        git_commit=True,)
    try:
            repo = Repo(git_dir)
            origin =repo.remote(name="origin")
            origin.push()
            print("Pushed Sucessfully!")
    except:
            print("Error occured while pushing repository to origin")