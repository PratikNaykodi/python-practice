# 3. Design a Python application where multiple threads update a shared variable.

# Use a Lock to avoid race conditions.
# Each thread should increment the shared counter multiple times.
# Display the final value of the counter after all threads complete execution.

# Import threading module
import threading

# Shared variable
Counter = 0

# Create lock object
Lock = threading.Lock()

# Thread function
def Increment():
    global Counter

    for _ in range(100000):
        with Lock:
            Counter = Counter + 1


# Main function
def main():
    # Create threads
    Thread1 = threading.Thread(target=Increment)
    Thread2 = threading.Thread(target=Increment)
    Thread3 = threading.Thread(target=Increment)

    # Start threads
    Thread1.start()
    Thread2.start()
    Thread3.start()

    # Wait for all threads to complete
    Thread1.join()
    Thread2.join()
    Thread3.join()

    # Display final value
    print("Final Counter Value :", Counter)

# Program execution starts from here
if __name__ == "__main__":
    main()