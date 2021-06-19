import socket
import sys

Client = socket.socket()
host = '192.168.56.103'
port = 4848

try:
    Client.connect((host,port))
    print (' Successfull Connect! ')
except socket.error as e:
    print ( str(e) )

loop = True

while loop:
    print ('\n Welcome to math calculator python ')
    print (' 1. Logarithmic expression ')
    print (' 2. Square Root ')
    print (' 3. Exponential expression ')
    print (' 4. Power Of ')
    print (' 9. Exit ')
    
    ans = input ('\n Enter your choice : ' )
    Client.send(ans.encode())

    if ans == '1':
        #log
        print ('\n [+] Log Function ')
        numb = input('\n Enter Number : ')
        b = input('\n Enter base : ')
        Client.sendall(str.encode('\n'.join([str(numb), str(b)])))
        tot = Client.recv(1024)
        print ( ' Answer for log ' + numb + ' base ' + b + ' : ' + str(tot.decode()))

    elif ans == '2':
        #Suare Root
        root = True
        while root:
            print ('\n [+] Square Root Function ')
            numb = input ('\n Enter Number : ')
            if float(numb) <  0:
                print('\n Negative Number Cant Be Square Root')
            else:
                root = False
                Client.send(numb.encode())
                tot = Client.recv(1024)

        print ( ' Answer for sqrt ' + numb +' : ' + str(tot.decode()))


    elif ans == '3':
        #exponen
        print ('\n [+] Exponential Function ')
        numb = input ('\n Enter Number : ')
        Client.send(numb.encode())
        tot = Client.recv(1024)

        print ( ' Answer for exp ' + numb + ' : ' + str(tot.decode()))

    elif ans == '4':
        #Power Of
        print ('\n [+] Power Of Function ')
        numb = input('\n Enter Number : ')
        p = input('\n Enter Power Of : ')
        Client.sendall(str.encode('\n'.join([str(numb), str(p)])))
        tot = Client.recv(1024)
        print ( ' Answer for ' + numb + ' pow of ' + p + ' : ' + str(tot.decode()))

    elif ans == '9':
        #exit
        Client.close()
        sys.exit()
    else:
        print ('\n Invalid input please try again !')

    input ( '\n Press Enter to Continue .. ')
