import socketserver

# load database from textfile
# open file
f = open("data.txt", "r")

# read file into a string
# dataBase = f.read()

dataBase = list()


while True:
    line = f.readline()
    # if no more lines to read, stop loop
    if (line == ""):
        break
    # if there is no name dont add to database
    if (line[0] == "|"):
        continue
    else:
        # each person will be their own list (db is a list of lists)
        personList = [data.strip() for data in line.split("|")]

        # person must have three "|" symbols i.e. a list of length four
        if (len(personList) != 4):
            continue

        canAdd = True
        # check if name already exists
        for names in dataBase:
            if (names[0] == personList[0]):
                canAdd = False
                break
        
        if (canAdd):
            dataBase.append(personList)



# process commands
def serverFunctions(command):
    # remove bytes notation b'...'
    command = command[2:-1]

    # split command into list of data
    commandList = command.split("|")
    option = commandList[0]

    # match commands to function and return function results
    # can pop the command number because functions knows of themselves
    if option == '1':
        commandList.pop(0)
        message = findCustomer(commandList)
    elif option == '2':
        commandList.pop(0)
        message = addCustomer(commandList)
    elif option == '3':
        commandList.pop(0)
        message = delCustomer(commandList)
    elif option == '4':
        commandList.pop(0)
        message = updateCustomerAge(commandList)
    elif option == '5':
        commandList.pop(0)
        message = updateCustomerAddress(commandList)
    elif option == '6':
        commandList.pop(0)
        message = updateCustomerPhone(commandList)
    elif option == '7':
        message = printReport()

    return message

# find a customer in database
def findCustomer(arr):
    customerName = arr[0]
    # loop through the database and see if there is a name that matches
    i = 0
    for name in dataBase:
        # if customer found, send customer info to client
        if dataBase[i][0] == customerName:
            return "|".join(dataBase[i])
        else:
            i = i + 1
            continue
    # if customer not found
    return "Customer " + customerName + " not in database."

# add a customer
def addCustomer(arr):
    customerName = arr[0]
    if (customerName == ""):
        return "Customer needs a name to be stored in database."
    # loop through database to ensure person doesnt exist yet
    i = 0
    for name in dataBase:
        if dataBase[i][0] == customerName:
            return "Customer already exists."
        else:
            i = i + 1
    # if we got here, name is not in database
    dataBase.append(arr)
    return "Customer " + customerName + " successfully added to database."

def delCustomer(arr):
    customerName = arr[0]
    i = 0
    for name in dataBase:
        if dataBase[i][0] == customerName:
            dataBase.pop(i)
            return "Customer " + customerName + " successfully deleted from database."  
        else:
            i = i + 1 
    return "Customer does not exist"

def updateCustomerAge(arr):
    customerName = arr[0]
    i = 0
    for name in dataBase:
        if dataBase[i][0] == customerName:
            dataBase[i][1] = arr[1]
            return "Customer " + customerName + "'s age successfully updated."
        else:
            i = i + 1
    return "Customer does not exist"

def updateCustomerAddress(arr):
    customerName = arr[0]
    i = 0
    for name in dataBase:
        if dataBase[i][0] == customerName:
            dataBase[i][2] = arr[1]
        else:
            i = i + 1
    return "Customer does not exist"

def updateCustomerPhone(arr):
    customerName = arr[0]
    i = 0
    for name in dataBase:
        if dataBase[i][0] == customerName:
            dataBase[i][3] = arr[1]
        else:
            i = i + 1
    return "Customer does not exist"

def printReport():
    i = 0
    report = "\n**Python DB Contents**\n"
    # sort the people
    dataBase.sort()
    for person in dataBase:
        report = report + "|".join(dataBase[i]) + "\n"
        i = i + 1
    return report
 

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The request handler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        self.result = serverFunctions(str(self.data))


        self.request.sendall(bytes(self.result, 'utf-8'))

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server:
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

    




