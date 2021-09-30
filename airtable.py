#%%
import requests
import json
import pandas as pd

class Airtable():
    def __init__(self):
        self.set_api_key()
        self.set_base_id()
        self.set_table_name()
        self.url = "https://api.airtable.com/v0/" + self.base_id + "/" + self.table_name
        self.headers = {"Authorization": "Bearer " + self.api_key}
    
    def set_api_key (self, api_key = False):
        if not api_key:
            with open('keys/api_key.txt') as f:
                self.api_key = f.read()
        else:
            self.api_key = api_key

    def set_base_id(self,base_id = False):
        if not base_id:
            with open('keys/base_id.txt') as f:
                self.base_id = f.read()
        else:
            self.base_id = base_id

    def set_table_name(self,table_name = False):
        if not table_name:
            with open('keys/table_name.txt') as f:
                self.table_name = f.read()
        else:
            self.table_name = table_name

    def set_url():
        if not(self.base_id):
            self.set_base_id()
        if not(self.table_name):
            self.set_table_name()
            
        self.url = "https://api.airtable.com/v0/" + self.base_id + "/" + self.table_name
        


    def get_table(self,params= (),table_name = False):
        pass

    def get_dataframe(self):
        pass
    
    





if __name__=="__main__":
    air = Airtable()
    

# %%
