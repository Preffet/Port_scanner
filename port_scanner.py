import socket

def get_open_ports(target, port_range, verbose=False):
    open_ports = []
    # IPv4 TCP connection
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = target

    #if verbose mode is set to False, return a list of open ports:
    if(verbose == False):
        #check all ports in the given range
        for i in range(port_range[0], port_range[1]+1):
            if s.connect_ex((host, i)):
                print(str(i)+" port is closed")
            else:
                open_ports.append(i)
                print(str(i)+" port is open")
        return(open_ports)



