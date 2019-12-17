import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server = '91.92.136.39'
def pscan (port):
    try:
        s.connect((server,port))
        return True
    except:
        return False
for x in range(1,444):
    if pscan(x):
        print('port',x,'is open')
    else:
        print('port',x,'is closed')


