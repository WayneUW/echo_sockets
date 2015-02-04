import socket
import sys


def client(msg, log_buffer=sys.stderr):    #stderr is typically used instead of stdout for messages captured during execution
    server_address = ('localhost', 10000)
    
    sock = socket.socket(    # these arguments are constants
        socket.AF_INET,
        socket.SOCK_STREAM,
        socket.IPPROTO_IP)

    print >>log_buffer, 'Connecting to {0} port {1}'.format(*server_address)

    sock.connect(('127.0.0.1', 10000))

    try:
        print >>log_buffer, 'Sending "{0}"'.format(msg)
        sock.sendall(msg)    # sends the whole message created when you ran the script
                             # the server will receive it and send back to you in 16 byte chunks 

        whole = ''    # start with an empty string
        done = False    # used to set up the while statement
        while not done:
            chunk = sock.recv(16)    # receive 16 bits at a time
            print >>log_buffer, 'Received "{0}"'.format(chunk)    # print each chunk as you get it
            whole += chunk    # store those 16 bits to the assignment named whole to accumulate the message
            if whole == msg:    # compare whole to the message to check if the entire message was sent
                done = True    # if the entire message is sent, end the loop
    finally:
        print >>log_buffer, 'Closing socket'
        sock.close()


if __name__ == '__main__':
    if len(sys.argv) != 2:    # it's expecting the name of the file and your message
        usg = '\nType the following: python echo_client.py "type the message you want to send here"\n'
        print >>sys.stderr, usg
        sys.exit(1)    # if it doesn't get those items it will exit and display 1

    msg = sys.argv[1]    # of what is typed at the command line, the message is the 1st index
    client(msg)    # call the function with the message