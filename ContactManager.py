#!/usr/bin/env python
# [-*- coding: utf-8 -*-[]
"""
Contacts Manager + SMS.
Usage:
    contacts add -n ,<name> -p <phone_number>
    contacts search <name>
    contacts text <name> -m <message>...
    contacts --version
    contacts (-i | --interactive)
    contacts (-h | --help)


Options:
    -h, --help  Show this help message.
    --version   Show the version and exit.
    -i, --interactive   Interactive Mode
"""

import sys
import cmd
from docopt import docopt, DocoptExit

from sqlalchemy import *
db = create_engine('sqlite:///test7.db')
db.echo = True
metadata = MetaData(db)
session = create_session()

phone_book = Table('users', metadata,
    Column('user_id', Integer, primary_key=True, autoincrement=True),
    Column('name', String(40), nullable=False),
    Column('age', Integer, nullable=False)
)
phone_book.create()

class Contacts(object):
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    #def __repr__(self):
     #   return 'Article %d: "%s"' % (self.article_id, self.headline)


def docopt_cmd(func):
    """
    This decorator is used to simplify the try/except block and pass the result
    of the docopt parsing to the called action.
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
    intro = 'Welcome to Contacts Manager' \
        + ' Contacts Manager manages contacts for you and can send an SMS to any contact\n' \
        + ' (type help for a list of commands.)'
    prompt = '(Contact Manager) '
    file = None

    @docopt_cmd
    def do_add(self, arg):
        """
        Add contacts.
        Usage: add -n name -p phone_number
        """
        if isinstance(arg['<name>'], str) and arg['<phone_number>'].isdigit():
            print(arg)
            a1=Contacts(arg['<name>'],arg['<phone_number>'])
            session.save(a1)
            print 'Good Job'
        else:
            print "The name must be of type string and phone number type interger"

        

    @docopt_cmd
    def do_search(self, arg):
        """
        Add contacts.
        Usage: search <name>
        """

        print(arg)
    @docopt_cmd
    def do_text(self, arg):
        """
        Add contacts.
        Usage: text <name> -m <message>...
        """

        print(arg)
    
    @docopt_cmd
    def do_quit(self, arg):
        """Quits out of Interactive Mode."""

        print('Good Bye!')
        exit()

opt = docopt(__doc__, sys.argv[1:])


if opt['--interactive']:
    ContactManager().cmdloop()

print (opt)