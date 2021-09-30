#%%
from collections import OrderedDict
from airtable import Airtable
from user import User
# import requests

# %%
class Engine():
    def __init__(self):
        self.get_users()
        self.air = Airtable()
        self.air.get_dataframe()
    
    def get_users(self,num=10):
        users = []
        for i in range(num):
            users.append(User())
        self.users=users

    def get_table_tags(self):
        tags = self.air.table_df.obj_topics.dropna()

        t_dict = OrderedDict()
        for i,vali in enumerate(tags):
            for j,valj in enumerate(vali):
                if valj not in t_dict.keys():
                    t_dict[valj] =1
                else:
                    t_dict[valj] +=1
        self.table_tags = t_dict
    
    def set_user_tags_blank(self):
        if not self.table_tags:
            self.get_table_tags()
        
        clean_tags = self.table_tags
        for key in clean_tags.keys():
            clean_tags[key] = .1 #setting this to >0 to actaually give reccomendations to users with no read tags
        
        for user in self.users:
            user.tags_read = clean_tags


if __name__ == "__main__":
    eng = Engine()
    eng.get_table_tags()
    eng.set_user_tags_blank()
    



    air = eng.air
    df = air.table_df
    user0 = eng.users[0]
    # eng.air.get_dataframe()
# %%
