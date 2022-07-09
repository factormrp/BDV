from typing import List
import requests
import json

S_YR = "2019"
E_YR = "2022"

class Scraper:
    def __init__(self) -> None:
        self.url = "https://api.bls.gov/publicAPI/v1/timeseries/data/"
        self.headers = {"Content-type":"application/json"}

    def get_series(self, id: str, startyear: str = S_YR,
        endyear: str = E_YR) -> dict:
            payload = json.dumps({"seriesid":[id],"startyear":startyear,
                "endyear":endyear})
            with requests.Session() as sesh:
                resp = sesh.post(self.url,data=payload,headers=self.headers)
            return json.loads(resp.text)

    def get_many_series(self, ids: List[str], startyear: str = S_YR,
        endyear: str = E_YR) -> dict:
            payload = json.dumps({"seriesid":ids,"startyear":startyear,
                "endyear":endyear})
            with requests.Session() as sesh:
                resp = sesh.post(self.url,data=payload,headers=self.headers)
            return json.loads(resp.text)
