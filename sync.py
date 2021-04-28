import subprocess
subprocess.run("git add .", shell=True)
subprocess.run('git commit -m "sync command used"', shell=True)
subprocess.run("git push", shell=True)
print('Code synced to github!')
