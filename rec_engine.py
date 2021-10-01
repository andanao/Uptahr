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
        self.article_id_list = self.air.table_df.index.tolist()
        self.make_tag_array()
    
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
        tag_df = pd.DataFrame(np.zeros([len(self.air.table_df),len(self.table_tags)]),
                        index = self.air.table_df.index,
                        columns=self.table_tags.keys())

        total_reads = self.air.table_df.iloc[:,-1].sum()
        for i,art_id in enumerate(tag_df.index):
            article_reads=self.air.table_df.iloc[i,-1]/total_reads
            for j,tag_id in enumerate(tag_df.columns):
                if isinstance(self.air.table_df.obj_topics[art_id],list):
                    if tag_id in self.air.table_df.obj_topics[art_id]:
                        tag_df.iloc[i,j] = article_reads

        self.tag_np = tag_df.to_numpy()
        self.tag_df = tag_df

    def read_article(self,art_id,user):
        user.articles_read.append(art_id)
        # self.air.table_df.
        self.air.table_df.loc[art_id,"read_count"] +=1
        if isinstance(self.air.table_df.obj_topics[art_id],list):
            for item in self.air.table_df.obj_topics[art_id]:
                user.tags_read[item] +=1



if __name__ == "__main__":
    eng = Engine()
    # eng.get_table_tags()
    # eng.set_user_tags_blank()
    # eng.get_article_reads()
    # eng.make_tag_array()
    # make user 0 read 20 random articles
    for i in np.random.randint(0,len(eng.article_id_list),size=20):
        eng.read_article(eng.article_id_list[i],eng.users[0])


    air = eng.air
    df = air.table_df
    user0 = eng.users[0]
    # eng.air.get_dataframe()
# %%

read_count_np = eng.air.table_df.iloc[:,-1].to_numpy()

# %%
