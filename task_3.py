import sys
from pathlib import Path
from colorama import init, Fore, Style


def print_directory_tree(directory: Path):
    """
    Prints the directory tree structure with colored output.

    Args:
        directory (Path): The path to the directory to visualize.
    """

    def _print_tree(current_dir: Path, level: int):
        # adding indent for correct visual formatting
        indent = "    " * level

        try:
            for item in current_dir.iterdir():
                if item.is_dir():
                    print(f"{indent}{Fore.BLUE}{item.name}{Style.RESET_ALL}")
                    _print_tree(item, level + 1)
                else:
                    print(f"{indent}{Fore.GREEN}{item.name}{Style.RESET_ALL}")
        except PermissionError:
            print(f"{indent}{Fore.RED}Permission denied: {current_dir}{Style.RESET_ALL}")

    # Print the root directory name
    print(f"{Fore.BLUE}{directory.name}{Style.RESET_ALL}")
    _print_tree(directory, 1)


def main():
    init(autoreset=True)

    if len(sys.argv) < 2:
        print(f"{Fore.RED}Invalid arguments provided.{Style.RESET_ALL} Usage: python hw03.py <directory_path>")
        sys.exit(1)

    dir_path = Path(sys.argv[1])

    if not dir_path.exists():
        print(f"{Fore.RED}The specified path does not exist.{Style.RESET_ALL}")
        sys.exit(1)
    if not dir_path.is_dir():
        print(f"{Fore.RED}The specified path is not a directory.{Style.RESET_ALL}")
        sys.exit(1)

    print_directory_tree(dir_path)


if __name__ == "__main__":
    main()