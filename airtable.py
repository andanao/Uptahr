#%%
import requests
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

    def set_url(self):
        if not(self.base_id):
            self.set_base_id()
        if not(self.table_name):
            self.set_table_name()
            
        self.url = "https://api.airtable.com/v0/" + self.base_id + "/" + self.table_name
        

    def get_table_all(self):
        params = ()
        airtable_records = []
        run = True
        while run is True:
            response = requests.get(air.url, params=params, headers=air.headers)
            airtable_response = response.json()
            airtable_records += (airtable_response["records"])
            if "offset" in airtable_response:
                run = True
                params = (("offset", airtable_response["offset"]),)
            else:
                run = False
        self.table_records = airtable_records
        return self.table_records

    def get_dataframe(self):
        airtable_rows = [] 
        airtable_index = []
        for record in self.airtable_records:
            airtable_rows.append(record["fields"])
            airtable_index.append(record["id"])
        df = pd.DataFrame(airtable_rows, index=airtable_index)
        df.columns = df.columns.str.replace('-', '_')
        self.table_df = df
        return self.table_df


if __name__=="__main__":
    import json
    air = Airtable()
    temp = air.get_table_all()
    df = air.get_dataframe()
