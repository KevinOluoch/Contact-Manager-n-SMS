**Contact Manager + SMS**
---------------------

**Andela Kenya Cohort X Boot Camp Project**

Contact manager is a console application for managing contactcs .
It should enables the user to manage contacts and send text messages.

**Required features**

A user should be able to add a person to the contacts list
with the following command: `add -n <name> -p <phone number>`
The command should save this contact in an SQLite database

A user should be able to search for a person’s contact by 
issuing a command: `search “Andela”` 
This should print  Andela’s phone number. 
In case we have more than one person using the name Andela, 
it should ask: Which Andela? [1] James [2] Hellen [3] Joshua i.e. James Andela, Hellen Andela, etc.

The system should be able to send simple one-way texts to the people in the 
contacts. e.g. a command `text James -m "Hi There"`
Using any appropriate SMS Gateway API e.g. Twilio, AfricasTalking, etc.
The contacts should be synced with Firebase (extra credit).



**Running ContactManager on your Computer**

Clone this repository

git clone

https://github.com/KevinOluoch/bc-10-Contact_Manager_n_SMS.git

Do a pip install for the dependancies

pip install -r requirements.txt

Then run ContactManager.py.


**Issues**

FireBase sync has not yet to be implemented.
