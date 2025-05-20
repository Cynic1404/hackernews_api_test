import requests
from api.api_base import ApiBase


class HackerNewsAPI(ApiBase):



    @classmethod
    def get_top_stories(cls, print_pretty=True):
        pretty_part_of_url=""
        if print_pretty:
            pretty_part_of_url = "?print=pretty"
        full_url = f"{ApiBase.root_url}/topstories.json{pretty_part_of_url}"
        response = requests.request("GET", url=full_url, headers=cls.headers, verify=False)
        return response.json()

    @classmethod
    def get_item(cls, item_id, print_pretty=True):
        pretty_part_of_url = ""
        if print_pretty:
            pretty_part_of_url = "?print=pretty"
        full_url = f"{ApiBase.root_url}/item/{item_id}.json{pretty_part_of_url}"
        response = requests.request("GET", url=full_url, headers=cls.headers, verify=False)
        return response.json()

    @classmethod
    def get_max_item(cls, print_pretty=True):
        pretty_part_of_url = ""
        if print_pretty:
            pretty_part_of_url = "?print=pretty"
        full_url = f"{ApiBase.root_url}/maxitem.json{pretty_part_of_url}"
        response = requests.request("GET", url=full_url, headers=cls.headers, verify=False)
        return response.json()




