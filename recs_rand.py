#%%
import numpy as np
import pandas as pd
#%%
class User:
    def __init__(self) -> None:
        self.id = np.random.randint(10000)
        self.articles_read = []
        # self.likes = np.zeros(10) # 
        self.likes = {}



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
        tags = ["ready",
                "linear",
                "crop",
                "host",
                "unique",
                "multi",
                "affect",
                "floor",
                "form",
                "treaty"]
        self.df = pd.DataFrame(np.random.randint(0,2,size=(10, 10)),
                                index = np.random.randint(0,100000,size=(10)),
                                columns=tags)
                    
        self.df["num_read"] = np.random.randint(0,1,size=(10))



    def article_read(self, art_id,user):
        """Mark the article as read by the user, increase the popularity of the article"""
        user.articles_read.append(art_id)
        self.df.loc[art_id].num_read += 1
        for i, tag in enumerate(self.df.columns[:-1]): #should get the # or tags, probably should have a better way if more things are going to be added to the DB
            if self.df.loc[art_id][i]:
                # print(val)
                if tag in user.likes:
                    user.likes[tag] += 1
                else:
                    user.likes[tag] = 1 #set to one increment later

        


    def suggest_articles(self,user):
        """suggest an article to a user"""
        

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