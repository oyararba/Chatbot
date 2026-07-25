# Chatbot
Helping users find a lost item

### A. Setup / installation instructions
- Python 3.10+ (I used Python 3.14) [installer](https://www.python.org/downloads/)

### B. Brief explanation of approach
My approach is a CLI-based customer support tool designed to help a customer find a lost package with minimal user friction. The overarching architecture simulates a backend database using in-memory object lookups to prioritize quick prototyping and easy reproducibility. The main program flow is in 3 steps: secure user authentication via standard libraries, data retrieval using in-memory objects and caching mechanism, and fault tolerant user interface that maps human-readable inputs to product IDs to fetch last location and relevant assitance tools to help customer find lost package.

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


