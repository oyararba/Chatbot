# Chatbot
Helping users find a lost item

### A. Setup / installation instructions
- Python 3.10+ (I used Python 3.14) [installer](https://www.python.org/downloads/)

### B. Brief explanation of approach
My approach simulates a database-driven supprot flow that prioritizes input flexibility and fault tolerance. 

- I use secure authentitcation with Python's getpass which hides the password. I apply a basic normalization to the raw inputs, as well as identifying and preventing basic SQL-injection based attacks before granting access to the user.
- I used hardcoded dictionaries in place of a real database connection, and this was primarily to keep the design simple and easily reproducible. NOTE: This is actually something I'd like to go more in depth on if I had more time.
- I map product IDs, which, in the real world, tend to not be human-readable by keeping two lists, one with the IDs, and one with the names corresponding. This could also be done in a dictionary, which would have been faster with complexity O(1) rather than O(N) with the list, but since N is so small in this case (order of 10 or less), I decided to not go more in depth on it. NOTE: If I was scaling this system even further I'd add this feature to reduce latency.
- I keep a cache of recently polled "recent purchases", with the idea that a user might ask for several items that might be lost, saving me time from a database query. This also allows me to have a faster "re-entry time" for when a user doesn't respond in a understandable way when prompted if their item is in the list of retrieved items.
- I also allow for a user to, instead of answering "yes or no" to the prompt, to *also* have the ability to just paste the number. This was done with the UX in mind that they might not want to go through several hoops but rather just type the product when they see it.
- For UX, I also make it so that the user doesn't have to input the specific order ID in order to find their data, this is because usually those IDs are complicated and long. Instead, showing the recently purhcased values from that username and password (which we got from login) allows the finding of a lost item to be more frictionless on the user, which would improve UX. NOTE: The object lookup tables/dictionaries also have a "time of order", and the statuses of the items has an "ARRIVED" section. If I got more in-depth to this, I'd hone in on what items they'd *likely* be asking for, without displaying as many of their previous purchases i.e if an item is arrived, and they say lost, you can "short circuit" to a ticket with a support line rather than waiting through my display of items, reducing friction even further, making it more personalized. 
-  I allow the user to be more flexible with their affirmations or denials, allowing "yes", "ye", "yess", "y","yep", "yeah" to all mean "yes". These all stem from different ways I'd say yes in a hurry, and also allows the user to be a bit more comfortable when operating the software that I'm making. Notably, small errors like another s at the end WILL end up in yes, same with another o at the end of no (noo). In those cases it's clear what the customer *meant* to say, and being stuck on the semantics *there* would add more unnecessary frustration and friction.

### C. Screenshots of chatbot in action
Figure 1: UX without needing for "yes and no" 
<img width="742" height="136" alt="figure1" src="https://github.com/user-attachments/assets/e8f807a0-d940-432b-acc8-e2327dfe76dc" />
Figure 2: Preventing SQL injection
<img width="368" height="68" alt="figure2" src="https://github.com/user-attachments/assets/0d138ae0-bf01-4730-a2c6-735964fd8988" />
Figure 3: "Everything is done properly" path
<img width="688" height="172" alt="figure3" src="https://github.com/user-attachments/assets/8652be34-c224-4e3c-b138-87ec3fcaf616" />
Figure 4: If user identifies that their missing object is in the list, they're re-queried to select the right answer rather than restart the entire "is it in this list" query.
<img width="683" height="289" alt="figure4" src="https://github.com/user-attachments/assets/5dfd2c86-109c-4164-a0a3-700ea2eb11bc" />
Figure 5: No recent orders, can't help customer find an item they didn't order.
<img width="936" height="88" alt="figure5" src="https://github.com/user-attachments/assets/242c85ee-d1a7-48fe-9b56-aeeb029723ab" />
Figure 6: Can't find the item in the list, requires external assistance
<img width="789" height="119" alt="figure6" src="https://github.com/user-attachments/assets/f0590cea-0947-47ef-a7f4-f4669b8d6eda" />

