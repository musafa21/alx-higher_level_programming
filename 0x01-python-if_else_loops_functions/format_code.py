#!/usr/bin/env python3

import os
import subprocess
import sys


def format_python_code(directory="."):
    # Find all Python files in the specified directory and its subdirectories
    python_files = [os.path.join(root, file) for root, dirs, files in os.walk(
        directory) for file in files if file.endswith(".py")]

    # Loop through each Python file and format it using autopep8
    for file_path in python_files:
        try:
            subprocess.run(["autopep8", "--in-place",
                           "--aggressive", file_path], check=True)
            print(f"Formatted: {file_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error formatting {file_path}: {e}")


if __name__ == "__main__":
    # Check if autopep8 is installed
    try:
        subprocess.run(["autopep8",
                        "--version"],
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       check=True)
    except FileNotFoundError:
        print("Error: autopep8 not found. Please install it using 'pip install autopep8'")
        sys.exit(1)

    # Get the directory path (default is the current working directory)
    target_directory = input(
        "Enter the target directory (default is current working directory): ").strip() or "."

    # Format Python code in the specified directory
    format_python_code(target_directory)
