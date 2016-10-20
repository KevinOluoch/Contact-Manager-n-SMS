#!/usr/bin/env python
# [-*- coding: utf-8 -*-[]
"""
Contacts Manager + SMS.
This Application can be used to store names 
and phone numbers in contacts,
and send SMS to a number in contacts.
Usage:
    contacts add -n ,<name> -p <phone_number>
    contacts search <name>
    contacts text <name> -m <message>...
    contacts --version
    contacts (-i | --interactive)
    contacts (-h | --help)
    contacts quit


Options:
    -h, --help  Show this help message.
    --version   Show the version and exit.
    -i, --interactive   Interactive Mode
"""

import sys
import cmd

from sqlalchemy import create_engine, MetaData, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from docopt import docopt, DocoptExit
from colorama import Fore, Back

import search
import sms

# Database connection
Base = declarative_base()
db = create_engine('sqlite:///:memory:', echo=False)
metadata = MetaData(db)
create_session = sessionmaker(bind=db)
session = create_session()


class Contacts(Base):
    """This class creates the contacts table in the database """


    __tablename__ = 'contacts'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    second_name = Column(String)
    phone_number = Column(Integer)
# Creating the Contacts table in Database
Base.metadata.create_all(db)
     

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block
    and pass the result of the docopt parsing to the called action.

    NOTE:
    Copied from, https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
    """


    def fn(self, arg):

        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class ContactManager(cmd.Cmd):
    """
    This class runs the User Interface and passes the input arguments to
    the appropriate functions, for execution.
     """

    
    print Fore.YELLOW +"  ___________________________________________________________________________________"
    print Fore.RED +   "  ___________________________________________________________________________________"
    print Fore.WHITE + "     ****    *****    ***    **  ********   **         ****  ********   ******       "
    print Fore.WHITE + "   **      **     **  ****   **     **     ** **     **         **     **    **      "
    print Fore.WHITE + "  **       **     **  ** **  **     **    **   **   **          **     **            "
    print Fore.GREEN + "  **       **     **  **  ** **     **   **  *  **  **          **      ** ***       "
    print Fore.WHITE + "  **       **     **  **   ****     **   ** *** **  **          **           **      "
    print Fore.WHITE + "   **      **     **  **    ***     **   **     **   **         **     **    **      "
    print Fore.WHITE + "     *****   *****    **     **     **   **     **     *****    **      ******       "
    print Fore.RED +   "  ___________________________________________________________________________________"
    print Fore.MAGENTA+"                    THE CONTACT MANAGER + SMS APP                                    "
    print Fore.YELLOW +"  !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
    
    print"""
    WELCOME TO CONTACTS MANAGER, THE APP THAT MANAGES YOUR CONTACTS.
    IT CAN BE USED TO SEND TEXT MESSAGES, TO PEOPLE IN YOUR CONTACTS.
    
    
    Commands:
            add -n ,<name> -p <phone_number>
            search <name>
            text <name> -m <message>...
            quit

    You can type "help" for information on the commands. 

    Recomended: Enter the phone number, in international format, 
                to enable texts i.e 2547xxxxxxxx (without +).  
    
    Options:
            --version
            (-i | --interactive)
            (-h | --help)
            
    """
  
    # Describing the command line promt
    prompt = '\nContact Manager >> '
    file = None

    @docopt_cmd
    def do_add(self, arg):
        """
        Adds an entry to contacts.
        Usage: add -n <name> -p <phone_number>
        """
        # The entries are first checked to assert their data type
        if isinstance(arg['<name>'], str) and arg['<phone_number>'].isdigit():
            # The user then enters their second name or it is set to 'unknown'
            print "WHAT IS %s'S SECOND NAME?" %(arg['<name>'])
            while True:
                second_name = raw_input("Enter Second name or 0 to ignore: ")
                if second_name == "0":
                    second_name="'unknown'"
                    break
                elif second_name:
                    break
                else: # This else statement ensures that the user inputs a second name or 0 (zero)
                    pass
            # The entry is saved to contacts
            entry = Contacts(name=arg['<name>'], second_name=second_name, 
                phone_number= arg['<phone_number>'])
            session.add(entry)

            print '%s has been saved to contacts' % (arg['<name>'])

        else:
            print "The name must be a string and phone number an interger"

        

    @docopt_cmd
    def do_search(self, arg):
        """
        Searches for an entry in contacts, using the first name of the entry.
        Usage: search <name>
        """

        found = search.search(arg, Contacts, session)
        # Printing the search result message 
        print found [1]


        

    @docopt_cmd
    def do_text(self, arg):
        """
        sends text messages to people entered in Contacts.
        Usage: text <name> -m <message>...
        """
        
        # Searching Contacts for the receipients number
        found = search.search(arg, Contacts, session)

        # If the receipients number is not in contacts, a message saying the same is sent
        if found[0] == 1:
            print found [1]
        # Sending text if receipients number is in contacts
        elif found[0] == 2:
            receiver_number = found[2]
            print "Texting %s ......" %(arg['<name>'])
            feedback = sms.text(receiver_number, ' '.join(arg['<message>']))
            print feedback[0]['status'] # Giving results of sending the text

        else:
            pass

        
    
    @docopt_cmd
    def do_quit(self, arg):
        """
        Quits out of Interactive Mode, thus ending the session
        Usage: quit
        """
        session.commit()
        print 'Good Bye!'
        exit()

opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    ContactManager().cmdloop()

print (opt)