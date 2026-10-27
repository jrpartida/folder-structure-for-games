import sys
from app import App

def main():
    if len(sys.argv) > 1:
        my_app = App(sys.argv[1])
        my_app.create_folder_structure()
    else:
        print("Argument Error.")

if __name__ == "__main__":
    main()