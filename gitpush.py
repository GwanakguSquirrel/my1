#%%
import os
import subprocess

def git_config(str_directory_path, name, email):
    os.chdir(str_directory_path)
    os.system("git config user.name " + name)
    os.system("git config user.email " + email)
    print("git config done")

def git_push(str_directory_path, id, password):
    name = "test"
    email = "test@test.com"
    os.chdir(str_directory_path)

    os.system("git add .")
    os.system("git commit -m 'e'")
    git_config(str_directory_path, name, email)

    os.system(
        "git push https://" + id +":" + password + "@github.com/GwanakguSquirrel/my1.git --all"
        )
    print("git push done")
# if your password or username contain @ replace it with %40