import re

from services import FreeGeoIPService, RdapArinService
from utils import IpInfoWriter


class LookUpController:

    def __init__(self, filename, rdap_only, geo_only):
        self.filename = filename
        self.rdap_only = rdap_only
        self.geo_only = geo_only
        self.all = not self.geo_only and not self.rdap_only

    def query(self):
        writer = IpInfoWriter()
        if self.all or self.geo_only:
            writer.append(FreeGeoIPService(self.payload).run())

        if self.all or self.rdap_only:
            writer.append(RdapArinService(self.payload).run())

        return writer

    @property
    def payload(self):
        pattern = re.compile(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})")
        with open(self.filename, "r") as f:
            results = []
            for line in f:
                ip = pattern.search(line)
                if ip:
                    results.append(ip[0])
        return results
