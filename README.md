**Contact Manager + SMS**
---------------------

**Introduction**

"Contact manager  + SMS" is a console application for managing contacts.
It enables the user to manage contacts and send text messages.

**Features**

It has the following features

 - A user should be able to add a person to the contacts list with the
   following command: `add -n <name> -p <phone number>` The command
   should save this contact in an SQLite database
   
  
 - A user should be able to search for a person’s contact by  issuing a 
   command: `search “Andela”`  This should print  Andela’s phone number.
   In case we have more than one person using the name Andela,  it   
   should ask: Which Andela? [1] James [2] Hellen [3] Joshua i.e. James 
   Andela, Hellen Andela, etc.

   

 - The system should be able to send simple one-way texts to the people 
   in the  contacts. e.g. a command `text James -m "Hi There"` Using any
   appropriate SMS Gateway API e.g. Twilio, AfricasTalking, etc. The   
   contacts should be synced with Firebase (extra credit).

**Dependencies**

The app requires the following python packages:

*SQLAlchemy* -is a Python SQL toolkit and Object Relational Mapper that provides the full power and flexibility of SQL.

*docopt* -This package is a automatically creates a given command line interface

*colorama* -used to produce colored terminal text and cursor positioning 

**Installing and runnning ContactManager on your Computer**

Clone this repository
git clone
https://github.com/KevinOluoch/bc-10-Contact_Manager_n_SMS.git
Do a pip install for the dependancies
pip freeze > requirements.txt
Then run ContactManager.py -i.


**Issues**
FireBase sync has not yet to be implemented.
