#!/usr/bin/env python3

import os
import subprocess
import sys


def format_python_file(filename):
    # Check if the file exists
    if not os.path.isfile(filename) or not filename.endswith(".py"):
        print(f"Error: Invalid file path or {filename} is not a Python file.")
        sys.exit(1)

    try:
        # Run autopep8 for indentation and line length
        subprocess.run(
            [
                "autopep8",
                "--in-place",
                "--aggressive",
                "--max-line-length",
                "79",
                "--recursive",
                "--global-config",
                "/dev/null",
                filename,
            ],
            check=True,
        )

        # Run black for consistent code formatting
        subprocess.run(["black", "--line-length", "79", filename], check=True)

        print(f"Formatted: {filename}")
    except subprocess.CalledProcessError as e:
        print(f"Error formatting {filename}: {e}")


if __name__ == "__main__":
    # Check if autopep8 and black are installed
    try:
        subprocess.run(
            ["autopep8", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        subprocess.run(
            ["black", "--version"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
    except FileNotFoundError:
        print(
            "Error: autopep8 and/or black not found. Please install them using 'pip install autopep8 black'"
        )
        sys.exit(1)

    # Get the filename from the user
    target_file = input(
        "Enter the name of the Python file to be formatted (including extension .py): "
    ).strip()

    # Format the specified Python file
    format_python_file(target_file)
