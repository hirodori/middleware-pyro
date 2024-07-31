import subprocess

commands = [
    'python server.py 1 12340',
    'python server.py 2 12341',
    'python server.py 3 12342',
    'python server.py 4 12343'
]

for cmd in commands:
    subprocess.Popen(f'start cmd /c {cmd}', shell=True)
