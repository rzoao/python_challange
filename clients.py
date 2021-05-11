from abc import abstractproperty
from collections import deque, defaultdict
import requests


global cache


class LRUCache:

    def __init__(self):
        self.deque = deque()
        self.map = defaultdict(str)
        self.MAX_CACHE = 5000

    def fetch_data(self, key):
        value = self.map.get(key)
        if value:
            self.deque.remove(key)
            self.deque.appendleft(key)
            self.update_queue(key)

            return value
    
    def cache_data(self, key, value):
            self.map.update({key: value})
            self.deque.appendleft(key)
            self.update_queue(key)
    
    def update_queue(self, old_key):
        if len(self.deque) >= self.MAX_CACHE:
            old_key = self.deque.pop()
            self.map.pop(old_key)



cache = LRUCache()

def lru_cache(fn):
    def wrapper(other):
        result = cache.fetch_data(other.ip)
        if result:
            return result

        response = fn(other)
        cache.cache_data(other.ip, response)
        return response

    return wrapper

class ApplicationClient:

    @property
    @abstractproperty
    def service_url(self):
        pass

    def __init__(self, ip):
        self.ip = ip

    @lru_cache
    def request(self):
        prepare_request = self.service_url.format(self.ip)
        response = requests.get(prepare_request)

        return Response.from_http(response)


class RdapArinClient(ApplicationClient):

    service_url = "https://rdap.org/ip/{}"


class FreeGeoIPClient(ApplicationClient):

    service_url= "https://freegeoip.app/json/{}"


class Response:

    @classmethod
    def from_http(cls, response):
        content = response.content
        return cls(content, response.status_code)

    def __init__(self, body, status_code):
        self.body = body
        self.status_code = status_code
