import subprocess

command = input("Enter text: ")

subprocess.run(["echo", command], check=True)
