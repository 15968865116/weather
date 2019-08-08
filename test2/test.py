import requests
from bs4 import BeautifulSoup
import threading
from threading import Thread, Event
import logging
import time




def set_num(my_event):
    print('thread:starting')
    for i in range(4):
        if i == 2:
            my_event.set()
        print('Now is {}'.format(i))
        time.sleep(2)


if __name__ == '__main__':
    my_event = Event()
    x = threading.Thread(target=set_num,args=(my_event,))

    print("Main:before creating thread")
    x.start()
    #my_event.wait()
    print("Main:waiting threding end ")
    print("Main:all done")


