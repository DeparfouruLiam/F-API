from sqlmodel import Field, SQLModel
from account import *
from beneficiary import *

class User(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str = Field(index=True)
    password: str = Field(index=True)

#All users
# Liam = User("Liam", "furryfemboy", [LiamAccount],LiamAccount,[GhaziBeneficiary])
# Ghazi = User("Ghazi", "jadorelespieds", [GhaziAccount],GhaziAccount,[])
# Adam = User("Adam", "futa", [AdamAccount], AdamAccount,[])

CurrentUserId = 0
CurrentUserName = ""

def update_current_id(new_id):
    global CurrentUserId
    CurrentUserId = new_id

def update_current_name(new_name):
    global CurrentUserName
    CurrentUserName = new_name

def getCurrentUserId():
    global CurrentUserId
    return CurrentUserId

def getCurrentUserName():
    global CurrentUserName
    return CurrentUserName

CurrentUser = 0
#
# users = [Liam, Adam, Ghazi]

# def get_users():
#     return users

def get_current_user():
    return CurrentUser

# def add_user(username: str, password: str, iban: str):
#     new_account = add_account(iban)
#     new_user = User(username, password, [new_account],new_account,[])
#     users.append(new_user)
#     return new_user

def update_current_user(new_user):
    global CurrentUser
    CurrentUser = new_user
    return CurrentUser

# def user_from_username(username):
#     return next((x for x in get_users() if x.get_username() == username), None)
#
# def account_from_username(username):
#     account = user_from_username(username).get_main_account()
#     return account_from_iban(account.get_iban())
