import subprocess
import sys
import os
from pathlib import Path

# Collect command-line arguments (feature paths, tags, etc.)
command_args = list(filter(None, sys.argv[1:]))

# Determine repository root as the project directory (two levels up from this file)
REPO_ROOT = Path(__file__).resolve().parent.parent

# Ensure the working directory is the repository root to avoid PyCharm misconfig (e.g., 'C')
os.chdir(REPO_ROOT)

# Preserve simple arg handling for tag shorthand if user passes three args with a tag token
if command_args:
    if len(command_args) == 2:
        # Historically kept only the first arg when two provided; preserve minimal behavior
        command_args = command_args[:1]
    elif len(command_args) == 3 and command_args[2].startswith("@"):
        command_args = command_args[:1] + ["--tags=" + command_args[2]]

# Prefer invoking Behave via the current Python interpreter for environment consistency
cmd = [sys.executable, "-m", "behave"] + command_args

subprocess.run(cmd, cwd=str(REPO_ROOT))
