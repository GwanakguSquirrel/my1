#%%
import os
import subprocess

def git_config(str_directory_path, name, email):
    os.chdir(str_directory_path)
    os.system("git config user.name " + name)
    os.system("git config user.email " + email)

def git_push(str_directory_path, id, password):
    name = "test"
    email = "test@test.com"
    os.chdir(str_directory_path)

    os.system("git add .")
    os.system("git commit -m 'e'")
    git_config(str_directory_path, name, email)

    cmd = ["git push https://" + id +":" + password + "@github.com/GwanakguSquirrel/my1.git --all"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(3)
    o, e = proc.communicate()
    print(3)
    o = o.decode('ascii')
    print(3)
    e = e.decode('ascii')
    print(3)
    print("o:", o)
    print("e:", e)
