# insta360 - tcp hevc decoder
import socket
import cv2
import time


# create a tcp/ip socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
retryCounter = 0
maxRetries = 5

def instaTx(data):
    m = bytes.fromhex(data)
    sock.sendall(m)
    time.sleep(0.1)

def instaBuff():
    # clear the rx buffer again before we start to rx the hevc data stream
    print("ask for data packet")
    instaTx('1c000000040000010002180000800000100130283809400148285012')
    instaTx('07000000050000')
    instaTx('130000000400000800021900008000000a010b')
    instaTx('2e0000000400000900021a00008000000a0607271215181f1212aa010c10900319111111111111a13ff8010a1801')
    instaTx('2e0000000400000900021b00008000000a0607271215181f1212aa010c10900319111111111111a13ff8010a1807150000000400000800021c00008000000a0342465d')
    instaTx('130000000400000800021d00008000000a010b')

def instaInit():
    with open("data.bin", "wb") as file:
        data = sock.recv(999999) # clear input buffer
        # handshake start
        print("sync started")
        instaTx('1100000006000073794e63654e64696e53')
        data = sock.recv(17)
        if(data == bytes.fromhex('1100000006000073794e63654e64696e53')):
            print("sync ok")
        else:
            print("sync error")
            global retryCounter
            global maxRetries
            if(retryCounter <= maxRetries):
                retryCounter = retryCounter + 1
                instaInit()
            exit(-1)
        
        print("handshake started")
        #maybe handshake is not needed
        # instaTx('07000000050000')
        # instaTx('140000000400000800020000008000000a022430')
        # instaTx('360000000400000800020100008000000a24010203060b0c0d0e0f111314161e24252628292a3031323a3b3c424344464c525355585d')
        # instaTx('100000000400000f0002020000800000')
        # instaTx('07000000050000')
        # instaTx('1f0000000400000700020300008000000a020c0d120960bea4e0960668901c')
        # instaTx('130000000400000800020400008000000a010b')
        # instaTx('120000000400005300020500008000000801')
        # instaTx('07000000050000')
        # instaTx('120000000400005300020600008000000802')
        # instaTx('07000000050000')
        # instaTx('360000000400000800020700008000000a24010203060b0c0d0e0f111314161e24252628292a3031323a3b3c424344464c525355585d')
        # instaTx('390000000400000a00020800008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1001')
        # instaTx('120000000400001100020900008000000801')
        # instaTx('390000000400000a00020a00008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1006')
        # instaTx('120000000400001100020b00008000000802')
        # instaTx('390000000400000a00020c00008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1008')
        # instaTx('390000000400000a00020d00008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1003')
        # instaTx('390000000400000a00020e00008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1005')
        # instaTx('390000000400000a00020f00008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1007')
        # instaTx('390000000400000a00021000008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1002')
        # instaTx('390000000400000a00021100008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1004')
        # instaTx('390000000400000a00021200008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1009')
        # instaTx('390000000400000a00021300008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a100c')
        # instaTx('390000000400000a00021400008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a100d')
        # instaTx('390000000400000a00021500008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1011')
        # instaTx('390000000400000a00021600008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1012')
        # instaTx('390000000400000a00021700008000000a250102030405060708090a0b0c0d0e0f12141518191a1b1c1d1e1f202122232425262728292a1015')
        print("handshake ok")

        instaBuff()
        
        print("rx first data packet")

 

        while 1:
            data = sock.recv(9999999)
            file.write(data)
            instaBuff() #here comes the magic
            print("rx a data packet")

# Connect the socket to the port where the server is listening
server_address = ('192.168.42.1', 6666) #wlan passwort 88888888
print('connecting to %s port %s' % server_address)
sock.connect(server_address)
instaInit()
