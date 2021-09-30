#%%
from airtable import Airtable
from user import User

# %%
class Engine():
    def __init__(self) -> None:
        self.get_users
    
    def get_users(self,num=10):
        self.users = []
        for i in range(num):
            self.users.append(User())



if __name__ == "__main__":
    eng = Engine()
    user0 = eng.users[0]
# %%
