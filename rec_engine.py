#%%
from collections import OrderedDict
import pandas as pd
import numpy as np

from airtable import Airtable
from user import User


# %%
class Engine():
    def __init__(self):
        self.get_users()
        self.air = Airtable()
        self.air.get_dataframe()
        self.get_article_reads()
        self.get_table_tags()

        self.set_user_tags_blank()
    
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

    def get_article_reads(self):
        """get the number of times each article has been read and attatch it to the df"""
        print("!! get_article_reads generateing random read numbers")
        self.air.table_df['read_count'] = np.random.randint(0,1000,size=len(self.air.table_df))

    def make_tag_array(self):
        """make tag array, used for calculating reccomendations based on article tags"""
        pass


if __name__ == "__main__":
    eng = Engine()
    # eng.get_table_tags()
    # eng.set_user_tags_blank()
    # eng.get_article_reads()



    air = eng.air
    df = air.table_df
    user0 = eng.users[0]
    # eng.air.get_dataframe()
# %%
tag_df = pd.DataFrame(np.zeros([len(eng.air.table_df),len(eng.table_tags)]),
                        index = eng.air.table_df.index,
                        columns=eng.table_tags.keys())
# %%
