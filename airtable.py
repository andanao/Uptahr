import requests
import json
import pandas as pd

class Airtable():
    def __init__(self,api_key = False, base_id = False) -> None:
        with open('keys/api_key.txt') as f:
            self.api_key = f.read()
        with open('keys/base_id.txt') as f:
            self.base_id = f.read()
        