import asyncio
from random import randrange
import socket
from time import sleep

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 11235))
sock2.bind(('localhost', 11234))


async def send():
    while 1:
        data_snd: str = str(randrange(1, 100000000))
        sock.sendto(data_snd.encode(), ("localhost", 11235))
        sleep(2)
        await rcv()


async def rcv():
    data_rcv, addr = sock.recvfrom(1024)
    print("received from: ", addr)
    print(data_rcv.decode())

loop = asyncio.get_event_loop()
loop.create_task(send())
loop.create_task(rcv())
loop.run_forever()





