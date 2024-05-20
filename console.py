#!/usr/bin/python3
"""Airbnb command-line interface using cmd module."""


import cmd
import json


class AirbnbCLI(cmd.Cmd):
    """
    Command interpreter for Airbnb.
    Attributes:
        prompt (str): The command prompt string.
        user_db_file (str): File path for storing user data.
        place_db_file (str): File path for storing place data.
    """
    prompt = "(hbnb) "
    user_db_file = 'users.json'
    place_db_file = 'places.json'

    def do_help(self, args):
        """List available commands."""
        print('\n')
        print("Documented commands (type help <topic>):")
        print("========================================")
        print("EOF  help  quit")

    def do_quit(self, args):
        """Exit the Airbnb CLI>"""
        print()
        return True

    def do_EOF(self, line):
        """Crtl+D command to exit the program"""
        print()
        return True

    def emptyline(self):
        """empty line after calling Enter"""
        pass


if __name__ == '__main__':
    AirbnbCLI().cmdloop()
