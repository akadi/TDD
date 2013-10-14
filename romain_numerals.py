# -*- coding: utf-8 -*-
# Author(s): Abdelhalim Kadi <kadi.halim@gmail.com>
#Convert arabic numbers into roman numbers.

#Constst
DICT_NUMS = { 1: u'I',
              2: u'II',
              3: u'III',
              4: u'IV',
              5: u'V',
              6: u'VI',
              7: u'VII',
              8: u'VIII',
              9: u'IX',
             10: u'X',
             50: u'L',
            500: u'D',
           1000: u'M'
         }

def get_romain_numerals(number):
    u"""
    This function is used for convert an arabic numbers into romain numbers.
        number - an arabic number.
        return - a romain representation for this number.
        Example: get_romain_numerals(1) --> u'I'.
    """
    repr_romain  = u''
    keys = sorted(DICT_NUMS.iterkeys())
    if number in keys:
        return  u'%s%s' % (repr_romain, DICT_NUMS.get(number, ''))
    else:
        #Look for the element in keys who is the closest to our number
        #We return Concatinating value  of element \
        #and  value of (number - key) if number-element in DICT_NUMS.keys()
        #else we recall get_romain_numerals with (number - key) argument.
        #(recursive function )
        i = 0
        j = 1
        while number not in xrange(keys[i], keys[j]):
            i = i + 1
            j = j + 1

        repr_romain = repr_romain + DICT_NUMS[keys[i]] + get_romain_numerals(number - keys[i])

        return repr_romain
