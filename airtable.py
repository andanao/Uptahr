import requests
import json
import pandas as pd

class Airtable():
    def __init__(self,api_key = False, base_id = False) -> None:
        if not api_key:
            with open('keys/api_key.txt') as f:
                self.api_key = f.read()
        else:
            self.api_key = api_key
        if not base_id:
            with open('keys/base_id.txt') as f:
                self.base_id = f.read()
        else:
            self.base_id = base_id
        

if __name__=="__main__":
    air = Airtable()
    