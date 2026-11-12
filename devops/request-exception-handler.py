# get a url about 60 secs delay and handle exception
import requests
api='https://google.com'
import time, logging

logging.basicConfig(filename='abc.log',level=logging.INFO)
i=3
while(i>1):
    try:
        resp=requests.get(api,timeout=10)
        if resp.status_code == 500:
            logging.error('caught http 500 error')
        elif resp.status_code == 200:
            logging.info('http succeeded')
    except requests.exceptions.ConnectionError:
        logging.info('ConnectionError')
    except requests.exceptions.InvalidJSONError:
        logging.info('InvalidJSONError')
    except requests.exceptions.HTTPError:
        logging.info('HTTP error')
    time.sleep(60)
