from .chatbot import return_command_response
import sys


def main():
    user_input_array = sys.argv
    user_input = " ".join(user_input_array)
    # switch based on flags -h, -v, -d
    if "-h" in sys.argv:
        print("Help")
        print("Flags:")
        print("-h: Help")
        print("-v: Version")
    elif "-v" in sys.argv:
        print("Version", "0.1")
    else:
        return_command_response(user_input)

