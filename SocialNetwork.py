# # define class
#     1. id:int
#     2. connections:list
#     3. user_name:string
# methods
#     1. get user name
#     2. get id
#     3. get connections
#     3. create connections (connection_id)


class User:
    def __init__(self, username, id):
        self.id = id
        self.username = username
        self.connections = []

    def GetUsername(self):
        return self.username

    def GetId(self):
        return self.id

    def GetConnections(self):
        return self.connections

    def CreateConnections(self,connection_username):
        return self.connections.append(connection_username)


class Network:
    def __init__(self):
        self.user_list = []

    def AddUsername(self, username):
        id = len(self.user_list)
        new_username = User(username, id)
        self.user_list.append(new_username)
        return self.user_list

    def PrintUsername(self):
        print("Users:")
        for user in self.user_list:
            print((str(user.GetUsername()) + " id:" + str(user.GetId())))

    def AddConnection(self, first_user, second_user):
        for user in self.user_list:
            if user.GetUsername() == first_user:
                user1 = user
        for user in self.user_list:
            if user.GetUsername() == second_user:
                user2 = user
        user1.CreateConnections(user2.GetUsername())
        user2.CreateConnections(user1.GetUsername())

    def PrintConnection(self, username):
        print("Connections: ")
        for user in self.user_list:
            if username == user.GetUsername():
                print(user.GetUsername() + "'s connections are")
                print(user.GetConnections())
                break
            else:
                print("This user has no connections")
def main():
    mynetwork =  Network()
    done =  False
    while not done:
        action = input("""\nWhat would you like to   do?
        Add a user (u), print users (p),
        add connection (c), print connections (pc),quit (q)?""")
if   action ==   "p":#call relevant methodelif action ==   "u":#call relevant methodelif action ==   "pc":#call relevant methodelif action ==   "c":#call relevant method (remember to take in   TWO usernames)elif action ==   "q":print("Sorry to   see you go   so   soon!")breakelse:print("Sorry, I  didn't understand that.")if   __name__ ==   '__main__':main()

my_network = Network()
my_network.AddUsername("emoSheena123")
my_network.AddUsername("blackskulls123")
my_network.AddConnection("emoSheena123","blackskulls123")
my_network.PrintUsername()
my_network.PrintConnection("emoSheena123")




# //attribute username list in constructor
# 1. Add a user
#     define method
#     input: username
#     calculate user id by getting length of the user_list
#     append a new user to user list:user_name
#     output: none
# 2. Print users
#     print user list
#     loop through the list
#     for each user: call internal methods to print out id+
# 3.Add connection
#     input:user_name1, username2
#     add to list of connections
#     loop through user_list and get their id
#     call createConnections method(id)
#     output: none
# 4. print connection
#     input: username
#     //get connections from the users
#     connections list
#     use get users method
