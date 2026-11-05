import subprocess

print("hello")

command = ["sudo", "-u", "postgres", "psql", "-c","SELECT*FROM users;"] 

result = subprocess.run(command, capture_output=True,text=True)

print(result.stdout)

