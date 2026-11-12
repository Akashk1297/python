import requests,logging

logging.basicConfig(filename='abc.log',level=logging.INFO)
url='https://jsonplaceholder.typicode.com/post'
try:
    resp=requests.get(url,timeout=10)
    print(resp.raise_for_status)
    if resp.status_code==200:
        logging.info("success %d",resp.status_code)
    elif resp.status_code==500:
        logging.error("http 500 error %d",resp.status_code)
    elif resp.status_code==404:
        logging.error("http 500 error %d",resp.status_code)
except requests.exceptions.RetryError:
    logging.error('RetryError')
except requests.exceptions.ConnectTimeout:
    logging.error('ConnectTimeout')
except requests.exceptions.InvalidJSONError:
    logging.error('InvalidJSONError')
