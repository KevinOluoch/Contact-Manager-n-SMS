#!/usr/bin/env python
# [-*- coding: utf-8 -*-[]
"""
Contacts Manager + SMS.
This Application can be used to store names and phone numbers in contacts
and send SMS to a number in contacts
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
from docopt import docopt, DocoptExit
from colorama import Fore, Back

import search
import sms

from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = create_engine('sqlite:///:memory:', echo=False)
metadata = MetaData(db)
create_session = sessionmaker(bind=db)
session = create_session()


class Contacts(Base):
    __tablename__ = 'contacts'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    second_name = Column(String)
    phone_number = Column(Integer)


Base.metadata.create_all(db)
     

def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
    NOTE: Copied from, https://github.com/docopt/docopt/blob/master/examples/interactive_example.py
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
    
    print Fore.YELLOW +"___________________________________________________________________________________"
    print Fore.RED +   "___________________________________________________________________________________"
    print Fore.WHITE + "   ****    *****    ***    **  ********   **         ****  ********   ******       "
    print Fore.WHITE + " **      **     **  ****   **     **     ** **     **         **     **    **      "
    print Fore.WHITE + "**       **     **  ** **  **     **    **   **   **          **     **            "
    print Fore.GREEN + "**       **     **  **  ** **     **   **  *  **  **          **      ** ***       "
    print Fore.WHITE + "**       **     **  **   ****     **   ** *** **  **          **           **      "
    print Fore.WHITE + " **      **     **  **    ***     **   **     **   **         **     **    **      "
    print Fore.WHITE + "   *****   *****    **     **     **   **     **     *****    **      ******       "
    print Fore.RED +   "___________________________________________________________________________________"
    print Fore.MAGENTA+"                  THE CONTACT MANAGER + SMS APP                                    "
    print Fore.YELLOW +"!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

    print"""
    Commands:
            add -n ,<name> -p <phone_number>
            search <name>
            text <name> -m <message>...
    Options:
            --version
            (-i | --interactive)
            (-h | --help)
            quit
    """

    intro = 'Welcome to Contacts Manager \n' \
        + ' Contacts Manager manages contacts for you and can send an SMS to any contact\n' \
        + ' You can type "help" for a list of commands.'
    prompt = '(Contact Manager) '
    file = None

    @docopt_cmd
    def do_add(self, arg):
        """
        Add contacts.
        Usage: add -n <name> -p <phone_number>
        """
        if isinstance(arg['<name>'], str) and arg['<phone_number>'].isdigit():
            print "What is %s's second name" %(arg['<name>'])

            while True:
                second_name = raw_input("Enter Second name or 0 to ignore: ")
                if second_name == "0":
                    second_name="unknown"
                    break
                elif second_name:
                    break
                else:
                    #no input
                    pass

            entry = Contacts(name=arg['<name>'], second_name=second_name, phone_number= arg['<phone_number>'])
            session.add(entry)

            print '%s has been saved to contacts' % (arg['<name>'] )
        else:
            print "The name must be of type string and phone number type interger"

        

    @docopt_cmd
    def do_search(self, arg):
        """
        Search for a contacts.
        Usage: search <name>
        """
        print arg['<name>']
        found = search.search(arg, Contacts, session)

        if found[0] == 1:
            print found [1]

        elif found[0] == 2:
            print found[1]

        else:
            pass

        #print search_results
        #print(arg)

    @docopt_cmd
    def do_text(self, arg):
        """
        sends texts to people in contacts.
        Usage: text <name> -m <message>...
        """

        found = search.search(arg, Contacts, session)
        if found[0] == 1:
            print found [1]
        elif found[0] == 2:
            receiver_number = found[2]
            print "Texting %s ......" %(arg['<name>'])
            feedback = sms.text(receiver_number, ' '.join(arg['<message>']))
            print feedback[0]['status']
        else:
            pass

        
    
    @docopt_cmd
    def do_quit(self, arg):
        """Quits out of Interactive Mode.
        Usage: quit
        """
        session.commit()
        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])


if opt['--interactive']:
    ContactManager().cmdloop()

print (opt)