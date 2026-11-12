import requests,logging
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter

session=requests.session()
retry=Retry(backoff_factor=1,total=3,status_forcelist=[400,500,404,509])
logging.basicConfig(filename='abc.log',level=logging.DEBUG)

url='https://jsonplaceholder.typicode.com/posts'

try:
    adapter=HTTPAdapter(max_retries=retry)
    session.mount("https://",adapter)
    resp=session.get(url)
    print(resp)
    logging.INFO(resp)
except requests.exceptions.RetryError:
    print('retry failed')
    logging.INFO('FAILED')
