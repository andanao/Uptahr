#%%
import numpy as np
import pandas as pd
from collections import OrderedDict
#%%
class User:
    def __init__(self) -> None:
        self.id = np.random.randint(10000)
        self.articles_read = []
        # self.likes = np.zeros(10) # 
        self.tags = OrderedDict()
        self.tags["ready"] =  0.1
        self.tags["linear"] = 0.1
        self.tags["crop"] = 0.1
        self.tags["host"] = 0.1
        self.tags["unique"] = 0.1
        self.tags["multi"] = 0.1
        self.tags["affect"] = 0.1
        self.tags["floor"] = 0.1
        self.tags["form"] = 0.1
        self.tags["treaty"] = 0.1
        
        #.1 to make the math work out just in case the user hasn't ever read anything



#%%
class ArticleDB:
    def __init__(self):
        self.test = 'a'
        self.load_db()
        self.make_users()
    
    def make_users(self,num=10):
        """"make a list of 10 users"""
        self.users = []
        for i in range(num):
            self.users.append(User())

        

    def load_db(self):
        """this should connect to airtable but for the moment it is just gen a random file"""
        self.tags = ["ready",
                "linear",
                "crop",
                "host",
                "unique",
                "multi",
                "affect",
                "floor",
                "form",
                "treaty"]
        self.df = pd.DataFrame(np.random.randint(0,2,size=(20, 10)),
                                index = np.random.randint(0,100000,size=(20)),
                                columns=self.tags)
                    
        self.df["num_read"] = np.random.randint(0,20,size=(20))



    def article_read(self, art_id,user):
        """Mark the article as read by the user, increase the popularity of the article"""
        user.articles_read.append(art_id)
        self.df.loc[art_id].num_read += 1
        for i, tag in enumerate(self.df.columns[:-1]): #should get the # or tags, probably should have a better way if more things are going to be added to the DB
            if self.df.loc[art_id][i]:
                user.tags[tag] += 1



    def suggest_articles(self,user,return_df=False):
        """suggest an article to a user"""
        art_np = db.df.iloc[:,:-1].to_numpy() #don't include the num read column
        pop_np = db.df.iloc[:, -1].to_numpy()
        pop_np = pop_np/pop_np.sum()
        wgt_np = np.matmul(np.diag(pop_np),art_np) #weighted based on popularity
        use_np = np.array(list(user.tags.values())) # it's gross just don't look pls
        suggestion_np = np.matmul(wgt_np, use_np) #weighted suggestions, get sorted list
        suggestion_df = pd.DataFrame(suggestion_np,index=df.index)
        suggestion_df.sort_values(suggestion_df.columns[0],ascending=False)
        suggestion_df.drop(user.articles_read,inplace=True)
        if return_df:
            return suggestion_df
        else:
            return suggestion_df.index.tolist()

    

    def suggest_article_new_user(self,user):
        """print out most popular articles"""
        pass





if __name__ == "__main__":
    db = ArticleDB()
    db.article_read(db.df.index[0],db.users[0])
    
    db.article_read(db.df.index[1],db.users[0])
    db.article_read(db.df.index[0],db.users[1])
    
    
    
    
    df = db.df
    user = db.users[0]
    sugg = db.suggest_articles(db.users[0])

#%%



# %%
