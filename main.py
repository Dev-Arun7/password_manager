
users = {}

def create_acc(username, password):
  users[username] = password
  if len(password) < 4:
    return (False, "Password too short")
  if users.get(username) == password:
    return (True, "OK")
  else:
    return (False, "Something went wrong")

def login():
  print("Login Page")
  username = input("Enter username: ")
  password = input("Enter password: ")

  usermatch = username in users

  if users.get(username) == password:
    passmatch = True
  else:
    passmatch = False
  
  if usermatch: # true
    if passmatch: # true
      print("you are loged in")
    else:
      print("worng password")
  else:
    print("Account not found")
# 
# unit test
# val = create_acc("user", "user@123")
# val = create_acc(None, "sls")
# print(val)



#login()
#print(users)

