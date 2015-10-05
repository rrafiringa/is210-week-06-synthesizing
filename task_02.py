#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Guests invite """


def prepare_email(appointments):
    """
    Prepare a list of invites to send via email
    Args:
        appointments (list): A list of two-item tuples.
    Returns:
        list: List of invites
    """
    return ['Dear {},\nI look forward to meeting \
with you on {}.\nBest,\nMe'.format(col[0], col[1]) \
    for col in appointments]


if __name__ == '__main__':
    for x in prepare_email([('Marlon','Monday, October 5, 2015 3:00PM'), \
	('Sophia','Tuesday, October 6, 2015 at 11:00AM')]):
        print x