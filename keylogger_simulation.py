log_file = "keystrokes.txt"

def start_logger():
    print("Safe Keylogger Simulation")
    print("Type 'exit' to stop\n")

    while True:
        user_input = input("Enter text: ")

        if user_input.lower() == "exit":
            print("Stopping...")
            break

        with open(log_file, "a") as file:
            file.write(user_input + "\n")

        print("Logged!\n")

if __name__ == "__main__":
    start_logger()
