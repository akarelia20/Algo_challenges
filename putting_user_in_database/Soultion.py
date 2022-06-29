class User:
    def __init__(self, name, username, email):
        self.name= name
        self.username= username
        self.email= email

class Userdatabase:
    def __init__(self):
        self.users = []

    def insert(self, user):
        i= 0
        while i < len(self.users):
            if self.users[i].name > user.name:
                break 
            i+=1
        self.users.insert(i,user)

Amee = User("Amy", "amyAA", "a.a@gmail.com" )
Carlie = User ("Carlie","catCat", "carlie@yahoo.com")
Dev = User("Dev","dd" "d@d.com")
Mary = User("mary", "mary12", "mary@yagoo.com")

database = Userdatabase()
database.users.append(Amee)
database.users.append(Carlie)


database.insert(Dev)
database.insert(Carlie)

print(database.users)


print(database.users[1].name)
