"""
    A Python template for organizing command-line scripts.

        Command-Line Options:
        --param_true: Optional flag that, when specified, sets the related action to True.
        text: A required string argument that represents a simple text input.
        input_file: A required file path argument; the script checks if the file exists.
        input_dir: A required directory path argument; the script checks if the directory exists.

    Examples:
        To run the script with minimal required arguments:
            python your_script_name.py "Example text" /path/to/inputfile.txt /path/to/inputdir

        To run the script with the optional flag and required arguments:
            python your_script_name.py --param_true "Example text" /path/to/inputfile.txt /path/to/inputdir

    Note:
        This script is designed to be a starting point for building more complex command-line tools.
        Replace 'your_script_name.py' with the actual name of this script when executing it.
"""

import argparse
import sys
import os

def file_exists(path: str) -> str:
    """Check if a file exists at the specified path. If not, raise an error."""
    if not os.path.isfile(path):
        raise argparse.ArgumentTypeError(f"The file {path} does not exist.")
    return path

def directory_exists(path: str) -> str:
    """Check if a directory exists at the specified path. If not, raise an error."""
    if not os.path.exists(path):
        raise argparse.ArgumentTypeError(f"The directory {path} does not exist.")
    return path

def print_args(args: argparse.Namespace) -> None:
    """Print all arguments and their values stored in the argparse.Namespace."""
    args_data = vars(args)
    for arg_name, arg_value in args_data.items():
        print(f"{arg_name}: {arg_value}")

def main(args: argparse.Namespace) -> None:
    """Main function that prints all arguments provided to the script."""
    print_args(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--param_true", action="store_true", help="Set the flag to make it true.")
    parser.add_argument("text", type=str, help="A simple string.")
    parser.add_argument("input_file", type=file_exists, help="The input file path.")
    parser.add_argument("input_dir", type=directory_exists, help="The root directory.")

    args = parser.parse_args()
    main(args)
