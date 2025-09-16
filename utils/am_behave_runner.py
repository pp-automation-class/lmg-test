import subprocess
import sys


command_args = list(filter(None, sys.argv[1:]))

if command_args:
    if len(command_args) == 2:
        command_args = command_args[:1]
    elif len(command_args) == 3 and command_args[2][0] == "@":
        command_args = command_args[:1] + [ "--tags="+ command_args[2] ]

    subprocess.run(["behave"] + command_args)
