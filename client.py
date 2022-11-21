import socket
import sys

HOST, PORT = "localhost", 9999

# go eternally until user quits with option 8
while (True):
    # menu
    print("\nPython DB Menu\n")
    print("1. Find customer")
    print("2. Add customer")
    print("3. Delete customer")
    print("4. Update customer age")
    print("5. Update customer adress")
    print("6. Update customer phone")
    print("7. Print Report")
    print("8. Exit")

    # user selection
    selection = int(input("\nSelect: "))

    # check what user wants
    if selection == 1:
        print("\nFind customer selected:")
        data = "1|" + input("\nEnter customer name: ").strip()
    elif selection == 2:
        print("\nAdd customer selected:")
        data = "2|" + input("Enter customer name: ").strip()
        data += "|" + input("Enter customer age: ").strip()
        data += "|" + input("Enter customer address: ").strip()
        data += "|" + input("Enter customer phone: ").strip()
    elif selection == 3:
        data = "3|" + input("Enter customer name: ").strip()
    elif selection == 4:
        data = "4|" + input("Enter customer name: ").strip()
        data += "|" + input("Enter customer age: ").strip()
    elif selection == 5:
        data = "5|" + input("Enter customer name: ").strip()
        data += "|" + input("Enter customer address: ").strip()
    elif selection == 6:
        data = "6|" + input("Enter customer name: ").strip()
        data += "|" + input("Enter customer phone: ").strip()
    elif selection == 7:
        data = "7"
    elif selection == 8:
        print("\nGood bye!\n")
        exit()

    # Create a socket (SOCK_STREAM means a TCP socket)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")

   


    print("Server Response: {}".format(received))

