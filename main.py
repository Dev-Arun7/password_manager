users = {}
def create_acc(username, password):
  if len(password) < 4:
    return (False, "Password too short")

  users[username] = password
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
#=============================================
# unit test - 1
print("Test1 create acc: ", end="")
flag = 0
# valid username & valid password
val = create_acc("user", "user@123")

if val[0] == True and val[1] == "OK":
  flag = 0
if flag == 0:
  print("passed")
else:
  print("Test failed")

#=============================================
# unit test - 2
# valid username & valid password
print("Test2 create acc: ", end="")
flag = 0
val = create_acc("user", "us1")

if val[0] == True and val[1] == "OK":
  flag = 0

# valid username & invalid password

if val[0] == False and val[1] == "Password too short":
  flag = 0

if flag == 0:
  print("passed")

