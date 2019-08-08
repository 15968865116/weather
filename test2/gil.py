import time
import threading

def get_detail_htm(url):
    print ("get detail html start")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print ("get detail url start")
    time.sleep(2)
    print("get detail url end")

if __name__ == "__main__":
    thread1=threading.Thread(target=get_detail_htm,args=("",))
    thread2 = threading.Thread(target=get_detail_url, args=("",))
    time1=time.time()
    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    print("time={}ms".format(time.time()-time1))