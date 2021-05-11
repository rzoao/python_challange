import json


class RdapPresenter:

    @classmethod
    def from_response(cls, ip, response):
        return cls(
            True,
            ip,
            response.body
        )

    def __init__(
        self,
        found,
        ip,
        body
    ):
        self._found = found
        self.ip = ip
        self._body = json.loads(body)

    def __repr__(self):
        result_json = json.dumps(self._body, indent=3)
        return f"{result_json}"
        
class GeoIPPresenter:

    @classmethod
    def from_response(cls, response):
        body = json.loads(response.body)
        return cls(
            True,
            **body
        )

    def __init__(
        self,
        found,
        **kwargs
    ):
        self._found = found
        # trading readability - thus maintainability - for speed (I'm short on time)
        # TODO: explicitly declare attributes
        for k, v in kwargs.items():
                setattr(self, "_"+k, v)


    def __repr__(self):
        if self._found:
            return f"{self.ip} {self.country_name}{self.country_code}{self.city}{self.region_name}{self.region_code}{self.zip_code}{self.time_zone}\n{self.latitude}{self.longitude}{self.metro_code}" # NOQA
        else:
            return f"no data found for {self.ip}"

    @property
    def ip(self):
        return self._ip

    @property
    def country_name(self):
        return f"belongs to {self._country_name}" if self._country_name else ""

    @property
    def country_code(self):
        return f"({self._country_code}) " if self._country_code else ""

    @property
    def region_code(self):
        return f"({self._region_code})" if self._region_code else ""

    @property
    def region_name(self):
        return self._region_name

    @property
    def city(self):
        return f"city of {self._city}, " if self._city else ""

    @property
    def zip_code(self):
       return f"{self._zip_code} -" if self._zip_code else ""

    @property
    def time_zone(self):
        return f" - Timezone: {self._time_zone}" if self._time_zone else ""

    @property
    def latitude(self):
        return f"lat: {self._latitude}, " if self._latitude else ""

    @property
    def longitude(self):
        return f"long: {self._longitude}" if self._longitude else ""

    @property
    def metro_code(self):
        return f" - metro code: {self._metro_code}" if self._metro_code else ""
