#%%
from airtable import Airtable
from user import User

# %%
class Engine():
    def __init__(self):
        self.get_users()
        self.air = Airtable()
    
    def get_users(self,num=10):
        users = []
        for i in range(num):
            users.append(User())
        self.users=users

    


if __name__ == "__main__":
    eng = Engine()
    user0 = eng.users[0]
    eng.air.get_dataframe(return=True)
# %%
