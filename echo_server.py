import socket
import sys


def server(log_buffer=sys.stderr):
    address = ('127.0.0.1', 10000)
    sock = socket.socket(    # these arguments are constants
                        socket.AF_INET,
                        socket.SOCK_STREAM,
                        socket.IPPROTO_IP)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    print >>log_buffer, "Making server on {0}:{1}".format(*address)

    sock.bind(address)
    sock.listen(1)
    
    try:
        while True:
            print >>log_buffer, 'Server waiting for a connection...waiting...'
            conn, addr = sock.accept()    # accepts client connection. tuple is new socket object and address(tuple of ip address, port)
            try:
                print >>log_buffer, 'Connection made on {0}:{1}'.format(*addr)

                while True:
                    data = conn.recv(16)    # chunk the client message into 16 bytes.
                    print >>log_buffer, 'Received "{0}"'.format(data)   # print those 16 bytes
                    
                    conn.sendall(data)    # send back those 16 bytes
                    if len(data)<16:   
                        print >>log_buffer, 'Message complete'             
                        break
            finally:
                conn.close()

    except KeyboardInterrupt:
        sock.close()


if __name__ == '__main__':
    server()
    sys.exit(0)    # a 0 means the script ended properly
