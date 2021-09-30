#%%
import numpy as np
from collections import OrderedDict

class User:
    def __init__(self) -> None:
        self.id = np.random.randint(10000)
        self.articles_read = []
        # self.likes = np.zeros(10) # 
        self.tags_read = OrderedDict()


if __name__=="__main__":
    user = User()
    print("User ID\t\t"+str(user.id))
    print("articles_read\t"+str(user.articles_read))
    print("tags_read\t"+str(user.tags_read))
