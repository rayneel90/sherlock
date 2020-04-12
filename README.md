# sherlock Web Application
Sherlock is a web-based application for searching individuals/entities in the 
banks Customer-database. It has following top-level features:
1. **Single Search:-** The primary feature. Search a single individual / entity
 from the existing customer database. It has following features that make it 
 distinct from other deduplication or database searcg algorithms
    * It allows partial name match, which is achieved through levenshtein 
    distance algorithm
    * It  provides a name matching score and a composite matching score, which 
    take into account all the information provided regarding the customer 
    during the search. Both these scores are normalized (as opposed to existing
     deduplication algorithm). 


## Quick Start
Here are the steps to run the project
1. copy the project
2. go through the todo list related to `config/settings.py` and make necessary changes    
3. 
     
### Apps
The project is distributed through following applications. 
* `Cust_auth`: Custom Authentication application. It contain of following 
features 
    1. client side password encryption with random salt
    2. Authentication using AD credentials through an web-api 
    
            The API authentication is implemented in UAT and PROD environment, 
            but in local environment the authentication is bypassed. For more
            details, check cust_auth/forms.py.
    