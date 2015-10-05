#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Program to create invitations """


def get_party_stats(families, table_size=6):
    """
    Args:
        families (list): A list of families invited.
        table_size (int): Number of seats per table
    Returns:
        tuple: Total number of guests and total number of tables
    """
    num_guests = len([members for family in families for members in family])
    zones = [-(-len(family)/table_size) for family in families]
    num_tables = reduce(lambda x, y: x + y, zones)
    print 'Total Number of guests: ' + str(num_guests) + \
        '\nSeats per table: ' + str(table_size) + \
        '\nTables per family: ' + str(zones) + \
        '\nTables to reserve: ' + str(num_tables) + '\n'
    return (num_guests, num_tables)


if __name__ == '__main__':
    FAM = [['Andre', 'Michelle', 'Donald', 'Trey'],
           ['Roberto', 'Candy', 'Cecilia', 'Amber', 'Anthony', 'Pedro'],
           ['Rakoto', 'Ketaka', 'Nirina']]
    print get_party_stats(FAM, 3)