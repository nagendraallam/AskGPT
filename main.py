from chatbot import return_command_response, return_explaination_response
import sys

# Reciveing user input from terminal
user_input_array = sys.argv

# merge user_input array
user_input = " ".join(user_input_array)

# switch based on flags -h, -v, -d
if "-h" in sys.argv:
    print("Help")
    print("Flags:")
    print("-h: Help")
    print("-v: Version")
    print("-e: Explaination (responds more in depth)")
elif "-v" in sys.argv:
    print("Version", "1.0.0")
elif "-e" in sys.argv:
    print(return_explaination_response(user_input))
else:
    print(return_command_response(user_input))
