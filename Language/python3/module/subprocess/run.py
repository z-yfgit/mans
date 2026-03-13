import subprocess

result = subprocess.run("date +'%Y-%m-%d %H:%M:%S.%6N'", shell=True, check=False)

print(result.stdout)