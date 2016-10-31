import requests
import sys
from datetime import datetime, timedelta
from pythonwhois import get_whois
from urllib.parse import urlparse


def load_urls4check(path):
    with open(path, 'r') as read_file:
        file_text = read_file.read()

    text_lines = file_text.split('\n')
    urls = filter(None, text_lines)
    return urls


def retrieve_domain(url):
    return urlparse(url).netloc


def is_server_respond_with_200(url):
    try:
        return requests.get(url).status_code == 200
    except (requests.exceptions.HTTPError,
            requests.exceptions.BaseHTTPError,
            requests.exceptions.ConnectionError):
        return False


def get_domain_expiration_date(domain_name):
    expiration_date = get_whois(domain_name)['expiration_date']
    return expiration_date[0]


def is_server_payed_for_month(domain_name):
    interval = 30
    next_month = datetime.now() + timedelta(interval)
    return get_domain_expiration_date(domain_name) >= next_month


def print_sites_data(sites):
    for site in sites:
        print("Url: {}".format(site['url']))
        print("Responds with 200(HTTP OK): {}".format(site['alive']))
        print("Domain is payed at least for a month:"
              " {}".format(site['payed']))

if __name__ == '__main__':
    if len(sys.argv) > 1:
        urls = load_urls4check(sys.argv[1])
        sites = []
        for url in urls:
            site = {}
            site['url'] = url
            site['alive'] = is_server_respond_with_200(url)
            domain = retrieve_domain(url)
            site['payed'] = is_server_payed_for_month(domain)
            sites.append(site)

        print_sites_data(sites)
