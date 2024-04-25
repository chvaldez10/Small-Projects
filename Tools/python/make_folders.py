"""
    Python script to generate folders with n iterations.

    Examples:
        To run the script with minimal required arguments:
            python make_folders.py "folder" 7 "/path/to/inputdir"

    Note:
        
"""

import argparse
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

def generate_folders(args: argparse.Namespace) -> None:
    folder_prefix = args.folder_prefix
    max = args.num_of_iterations
    root_dir = args.root_dir
    counter = 0
    
    return
    while counter < max:
        pass

def main(args: argparse.Namespace) -> None:
    """Main function that prints all arguments provided to the script."""
    generate_folders(args)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("folder_prefix", type=str, help="Prefix for folder name.")
    parser.add_argument("num_of_iterations", type=int, help="Number of iteration.")
    parser.add_argument("root_dir", type=directory_exists, help="The root directory.")

    args = parser.parse_args()
    main(args)
