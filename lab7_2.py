import subprocess

# Exercise 2: ls
subprocess.run(["ls"])

# Exercise 3: ls com um argumento
subprocess.run(["ls","-l"])

# Exercise 4: ls com múltiplos argumentos
subprocess.run(["ls","-l","solution"])

# Exercise 5: Informação do sistema
command = "uname"
commandArgument = "-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Excercise #6: Informação do espaço em disco
command = "ps"
commandArgument = "-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command, commandArgument])