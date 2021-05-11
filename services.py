import requests

from clients import FreeGeoIPClient, RdapArinClient
from presenters import RdapPresenter,GeoIPPresenter 


class ApplicationService:

    def __init__(self, payload):
        self.payload = payload


class FreeGeoIPService(ApplicationService):

    def run(self):
        enriched_ips = {}
        for ip in self.payload:
            response = FreeGeoIPClient(ip).request()
            if response.status_code == requests.codes.ok:
                geo_ip = GeoIPPresenter.from_response(response)
                enriched_ips.update({ip: geo_ip})

        return enriched_ips


class RdapArinService(ApplicationService):
    def run(self):
        enriched_ips = {}
        for ip in self.payload:
            response = RdapArinClient(ip).request()

            if response.status_code == requests.codes.ok:
                rdap = RdapPresenter.from_response(ip, response)
                enriched_ips.update({ip: rdap})

        return enriched_ips
