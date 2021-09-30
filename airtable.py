#%%
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

        self.get_table()
        self.url = "https://api.airtable.com/v0/" + self.base_id + "/" + self.table_name
        self.headers = {"Authorization": "Bearer " + api_key}
    
    def set_response(self):
        pass

    def set_table_name(self,table_name = False):
        if not table_name:
            with open('keys/table_name.txt') as f:
                self.table_name = f.read()
        else:
            self.table_name = table_name

    def get_table(self,params= (),table_name = False):
        

    def get_dataframe(self):
        pass
    
    





if __name__=="__main__":
    air = Airtable()


# %%
