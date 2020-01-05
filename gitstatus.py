import subprocess
import os

def git_status_check(str_directory_path):
    # change working directory
    os.chdir(str_directory_path)
    cmd = ['git', 'status']
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    o, e = proc.communicate()
    o = o.decode('ascii')
    e = e.decode('ascii')

    str_up_to_data = "nothing to commit, working tree clean"
    if len(o) == 0:
        return "not a git directory"
    if str_up_to_data in o:
        return "up to date"
    else:
        return "exist new thing"