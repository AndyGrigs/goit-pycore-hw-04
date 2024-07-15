import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def print_directory_structure(directory_path, tab=""):
    try:
        directory = Path(directory_path)
        if not directory.exists() or not directory.is_dir():
            print(f"{Fore.RED}Error: Path '{directory_path}' does not exist or is not a directory.")
            return

        items = sorted(directory.iterdir(), key=lambda e: e.is_file())

        for item in items:
            if item.is_dir():
                print(f"{tab}{Fore.BLUE}{item.name}/{Style.RESET_ALL}")
                new_prefix = f"{tab}   "
                print_directory_structure(item, new_prefix)
            else:
                print(f"{tab}{Fore.GREEN}{item.name}{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}An error occurred: {e}{Style.RESET_ALL}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <directory_path>{Style.RESET_ALL}")
    else:
        directory_path = sys.argv[1]
        print(f"{Fore.BLUE}{Path(directory_path).name}/{Style.RESET_ALL}")
        print_directory_structure(directory_path, "    ")
