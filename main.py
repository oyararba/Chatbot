
import getpass

USERS = {

    "admin":"password123",
    "user":"321drowssap",
    "account1":"ac1pw"

}

# username, productids paired index to index with their order date. in a db this would be separate columns.
# needs to be cleaned periodically, keep longer-term/old orders in archival database
RECENT_ORDERS = {

    "admin": [["8ABC","ASJC", "ABSC"], ["07/2026", "05/2026", "01/2026"]],
    "user":[[], []],
    "account1": [["7ABC"],["07/2026"]]

}

ITEMS = {

    "8ABC": "BRAND Laptop",
    "ASJC": "BRAND Monitor",
    "ABSC": "OTHERBRAND Keyboard",
    "7ABC": "NEWBRAND Water Bottle"

}

LAST_LOCATION = {

    "8ABC": "TRANSIT: San Francisco, CA",
    "ASJC": "TRANSIT: Sunnyvale, CA",
    "ABSC": "ARRIVED: New York, NY",
    "7ABC": "ARRIVED: San Diego, CA"

}

SITE_NUMBERS = {

    "San Francisco": "415-XXX-XXX",
    "Sunnyvale": "408-XXX-XXX",
    "New York": "917-XXX-XXX",
    "San Diego": "619-XXX-XXX"

}


# fetch the users password from their id, and check if that lines up with what we have in our "DB"
def verify_user(id, password):
    
    try:
        password_fetched = USERS[id]
        if(password_fetched == password):
            return True
        return False

    except KeyError:
        return False

def normalize_input(raw_text):
    if not raw_text:
        return ""

    # remove spaces in front and back and make lowercase
    clean_text = raw_text.strip().lower()

            # IF WE HAD A RULE THAT IT COULDNT CONTAIN PUNCTUATION:
            # import string
            # clean_text = clean_text.translate(str.maketrans('', '', string.punctuation))
            # # removes punctionation 
            # # FURTHER DETAIL:
            # #string.punctuation() contains all standard ASCII punctuation marks.
            # #str.maketrans('', '', string.punctuation) makes a translation table, with the first two parameters being 
            #     #PARAM 1: character to replace
            #     #PARAM 2: character to replace with 
            #     #PARAM 3: characters to delete entirely.
            
            # # .translate() applies that table onto clean_text.
    
    return clean_text
     

def login():

    # get credentials, this will be used to check orders 
    username = input("Username: ")
    password = getpass.getpass("Password: ") # no visual on password, part of python stl 

    # prevent SQL injection with input checking for known vulnerability exploits (this is not extensive, if i was using SQL for this i'd use a PreparedStatement)
    if "--" in password or "--" in username:
        print("Invalid login.")
        return None, None

    # normalize inputs
    username_normalized = normalize_input(username)
    password_normalized = normalize_input(password)

    # make sure the user is valid 
    valid = verify_user(username_normalized, password_normalized)

    if valid:
        return username_normalized, password_normalized
    else:
        print("Invalid login.")
        return None, None

def get_relevant_items(username):

    # get order list, which has the product ids,
    order_list = RECENT_ORDERS[username][0]
    # make presentable as well
    items_human_readable = []
    for id in order_list:
        items_human_readable.append(ITEMS[id].lower())

    # do not show product id to users, separate 
    return order_list, items_human_readable


GENERAL_HELP_LINE = "321-XXX-XXX"

def handle_last_known_location(id):
    try:
        print("The last status we saw was", LAST_LOCATION[id])
        #"TRANSIT: San Francisco, CA"
        # this could have been a regex for more efficiency but heres how it works
        location = LAST_LOCATION[id].split(":")[1].split(",")[0].strip()

        # we know its going to be "STATUS: LOCATION, CITY "
        # LAST_LOCATION[id] returns this ^, we split on the : so we get [STATUS, (LOCATION,CITY)], then I pick [1] (LOCATION,CITY) then I split it on "," so I get [LOCATION, CITY] \
        # then i get [0] which is LOCATION then I strip() it to clean up whitespace trailing. 

        location_number = SITE_NUMBERS[location]

        print(f"Here's the phone number of that facility, give them a call at {location_number} for further assistance.")
        
    except (KeyError, IndexError):
        print(f"Sorry, this item doesn't seem to have a last location in our system. Contact the general help line ({GENERAL_HELP_LINE}) for further support.")
        


relevant_items_backend_cache = {}
relevant_items_cache = {}


def user_interface(username):
    
    #check local cache first

    try:
        relevant_items_backend = relevant_items_backend_cache[username]
        relevant_items = relevant_items_cache[username]

    except KeyError:
        relevant_items_backend, relevant_items = get_relevant_items(username) 
        #place into cache for faster recovery next time 
        relevant_items_backend_cache[username] = relevant_items_backend
        relevant_items_cache[username] = relevant_items


    # find items recently purhcased that have not yet been marked RECEIVED
    # this assumes that the ORDERS table will be cleaned at some consistent intervals
    if(relevant_items):
        print("Items you've purchased:", relevant_items)
    if not relevant_items:
        print(f"You don't have any recent orders in our system. This might be an error, contact the general help line ({GENERAL_HELP_LINE}) for more support")
        return -1

    isIn = normalize_input(input("Is your lost package in this list? (Type 'quit' to quit) "))    
    # catch the case in which they dont listen to instructions and just give the name 
    if (isIn in relevant_items):
        index = relevant_items.index(isIn)
        handle_last_known_location(relevant_items_backend[index])
        return -1

    
    if (isIn == "quit"):
        return -1

    
    if isIn in ["yes", "ye", "yess", "y","yep", "yeah"]:

        if(len(relevant_items) > 1): # if its not obvious which one theyre talking about 

            print("Great, which one?")
            item = normalize_input(input())
            while(item not in relevant_items):
                print("Sorry, that items not in the list. Try again")
                item = normalize_input(input())

            index = relevant_items.index(item)
            # avoid letting the user pick indexing because they could a) not know 0 indexing (likely) and b) might fiddle around with -1 or other invalid indices
            handle_last_known_location(relevant_items_backend[index])

            return -1
        else: # only one item,  as the if not relevant_items is checked above

            
            handle_last_known_location(relevant_items_backend[0])

            return -1
    elif isIn in ["no","nah", "n","nope", "noo"]:

        print(f"It seems your item is not showing up in our system. Call the general helpline at {GENERAL_HELP_LINE} for more assistance")

        return -1
    else:
        print("I didn't catch that, could you say that again?")

    
        



if __name__ == "__main__":

    print("Hi, I'll be helping you try to find a lost package.")
    username, password = login()

    

    if username is not None and password is not None:
        

        while(user_interface(username) != -1):  
            pass

        print("Thanks for using our service.")


    

