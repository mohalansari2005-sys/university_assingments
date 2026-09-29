# Program 1
social_network = {
    "Ali": ['Nora', 'Fahad', 'Sara', 'Khalid'],
    "Ahmed": ['Nora', 'Khalid'],
    "Lela": ['Fahad', 'Sara'],
    "Sara": ['Lela', 'Nora', 'Ali'],
    "Nora": ['Sara', 'Ahmed', 'Ali'],
    "Khalid": ['Ali', 'Ahmed', 'Fahad'],
    "Fahad": ['Khalid', 'Ali', 'Lela'],
}

def add_user(network, x):
    if x not in network:
        network[x] = []
        
 
def get_friends(network, x):
    if x in network:
        friends = set(network[x])
        return friends  
    
def add_two_mutual_friends(network, f1, f2):
    if f1 in network:
        f1_friends = network[f1]
        f1_friends.append(f2)
    else:
        add_user(network, f1)
        f1_friends = network[f1]
        f1_friends.append(f2)
    
    if f2 in network:
        f2_friends = network[f2]
        f2_friends.append(f1)
    else:
        add_user(network, f2)
        f2_friends = network[f2]
        f2_friends.append(f1)

def remove_two_friends(network, f1, f2):
    if f1 in network:
        f1_friends = network[f1]
        if f2 in f1_friends:
            f1_friends.remove(f2)
    if f2 in network:
        f2_friends = network[f2]
        if f1 in f2_friends:
            f2_friends.remove(f1)
            
def printFriends():
    for member, friendslist in social_network.items():
        friends = ", ".join(friendslist)
        print( f"{member}'s friends are: {friends} ")
        
        
# Program2 
def update_dict(dict, subj):
    for subject, marklist in dict.items():
        if subject == subj:
            for x in range(len(marklist)):
                marklist[x]+= 5 
                
                
#Program 3 
# I have these two lists:
# A : [1,2,3,4,5] and B: [1,2,6,7,9]

def difference_between_two_lists(a, b):
    setA = set(a) 
    setB = set(b)
    
    return setA - setB 
def difference_betweeb_two_lists(b, a):
    
    setA = set(a) 
    setB = set(b)
        
    return setA - setB 
    
    
#program4 
# list approach:
def addStudentToList(studentList, studentId):
    for x in range(len(studentList)):
        if studentList[x] == studentId:
            return False        
        
    studentList.append(studentId)
    return True 
            
#set approach:
def addStudentToSet(studentSet, studentId):
    studentSet.add(studentId)# this has a time complexity of O(1) unlike the previous version which was O(n)
    return True


# Program 5
ali_movies = {"Inception", "Life of Pi", "The dark knight", "A Separation"}
my_movies = {"The dark knight", "12 Angry men", "Inception", "LOR:TT"}
mohammed_movies = {"LOR:TT", "Seven Samurai", "Inception", "The Matrix"}


def should_ali_watch(ali_movies, my_movies, mohammed_movies):
    shared_with_mohammed = ali_movies & mohammed_movies
    shared_with_me = ali_movies & my_movies

    # a tie favors watching
    return len(shared_with_me) >= len(shared_with_mohammed)


print("Should Ali watch Oppenheimer?", should_ali_watch(ali_movies, my_movies, mohammed_movies))

