import logging
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

logging.basicConfig(
    filename="health_check.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

ENDPOINT = "/endpoint"


def check_server(host):
    url = f"https://{host}{ENDPOINT}"

    retry_policy = Retry(
        total=3,
        connect=3,
        read=2,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
        allowed_methods=["GET"]
    )

    try:
        with requests.Session() as session:
            adapter = HTTPAdapter(max_retries=retry_policy)
            session.mount("https://", adapter)

            response = session.get(url, timeout=(3, 10))
            response.raise_for_status()

            data = response.json()

            logging.info(
                "%s: CPU=%s Memory=%s AppStatus=%s",
                host,
                data.get("cpu"),
                data.get("memory"),
                data.get("application_status")
            )

            return host, "SUCCESS", data

    except requests.exceptions.Timeout:
        logging.error("%s: Request timed out", host)

    except requests.exceptions.HTTPError as exc:
        logging.error("%s: HTTP error: %s", host, exc)

    except requests.exceptions.ConnectionError as exc:
        logging.error("%s: Connection error: %s", host, exc)

    except requests.exceptions.JSONDecodeError:
        logging.error("%s: Invalid JSON response", host)

    except requests.exceptions.RequestException as exc:
        logging.error("%s: Request failed: %s", host, exc)

    return host, "FAILED", None


def main():
    with open("python/abc.txt") as file:
        hosts = [line.strip() for line in file if line.strip()]

    with ThreadPoolExecutor(max_workers=20) as executor:
        futures = [executor.submit(check_server, host) for host in hosts]

        for future in as_completed(futures):
            result = future.result()
            print(result)


if __name__ == "__main__":
    main()
