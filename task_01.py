#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using the datetime module"""

import datetime
CURDATE = None


def get_current_date():
    """Our function doesn't take any parameters. And using
       datetime.date.today() to return the current day as a date object.

    Arg:
        CURDATE(date): Assign the value of today's date
    Return:
        function that returns todays day as a date
    Examples:
       >>> import task_01
       >>> print task_01.CURDATE
           None
       >>> task_01.get_current_date()
           datetime.date(2016, 10, 5)
       $ python -i task_01.py
           2016-10-05
    """
    date = datetime.date.today()
    return date
if __name__ == '__main__':
    CURDATE = datetime.date.today()
    print CURDATE
