"""
A module containing functions to extract information from a JSONlite file.

This module provides simple string parsing functions to help traverse and
extract information from a JSONLite file.

Developed by Al Palanuwech (ap689) and Professor Bracy for CS1110SP A1.

Author: Kene Chukwuma (ebc68) and Monalisa Almeida (mca74)
Date:   02/20/23
"""

#############################################################################
# Students DO NOT MODIFY the code below
#############################################################################
import string as str_mod
alp = str_mod.ascii_lowercase[:26]
ENCRYPT_AMOUNT = 4


def get_line(s, num):
    """
    Returns the contents at the line `num` in s.
    Precondition s: a string that contains a JSONLite
    Precondition num: an non-negative integer, which line number exists in s.
    """
    if num == 0:
        # first line won't have a newline
        str_to_find = str(num)
    else:
        str_to_find = '\n'+str(num)
    length = len(str_to_find)
    ind = s.index(str_to_find)
    start = s.index(':', ind)+1
    end_ind = s.index('\n', ind+length)
    return s[start:end_ind]


def encrypt_helper(s):
    """
    Mystery encrypt function helper
    Precondition s: s is a string
    """
    if s in alp:
        ind = alp.index(s)
        return alp[(ind+ENCRYPT_AMOUNT) % 26]
    return s


def encrypt(s):
    """
    Given an input string s,return the encrypted string of s based off of
    the function encrypt_helper
    Precondition s: s is a string
    """
    map_obj = map(encrypt_helper, s)
    return ''.join(map_obj)


def decrypt_helper(s):
    """
    Mystery decrypt function helper
    Precondition s: s is a string
    """
    if s in alp:
        ind = alp.index(s)
        return alp[(ind-ENCRYPT_AMOUNT) % 26]
    return s


def decrypt(s):
    """
    Given an encrypted string s, return the decrypted string of s.
    Precondition s: s is a string that is encrypted
    """
    map_obj = map(decrypt_helper, s)
    return ''.join(map_obj)

#############################################################################
# Students complete the functions below:
#############################################################################


def before_first(text, marker):
    """Returns: portion of `text` ending just before the first occurrence of
    `marker`.

    Precondition text: a string that contains at least one instance of `marker`
    Precondition marker: a string of length 1

    Examples:
        before_first("ab+c", "+") ---> 'ab'
    """
    return text[:text.index(marker)]



def after_first(text, marker):
    """Returns: portion of `text` starting just after the 1st occurrence of
    `marker`.

    Precondition text: a string that contains at least one instance of `marker`
    Precondition marker: a string of length 1

    Examples:
        after_first("ab+c", "+") ---> 'c'
            To be clear, that's a length-one string.
    """
    pos = text.index(marker) + (len(marker))
    return text[pos:]



def file_to_string(filename):
    """
    Returns the contents of a JSONLite file as a string

    Precondition filename: a string that is the filename of a JSONLite file that
    exists in the current directory
    """
    file = open(filename)
    name = file.read()
    file.close()
    return name



def get_value(s, keyword):
    """
    Given the contents of a line of JSONlite, return the value corresponding to
    the key `keyword` (as a string).

    Precondition s: a string containing contents from a single line from a
        JSONLite string
    Precondition keyword: a string made with only alphanumerical characters
        that is a valid keyword in s
    Example:
        get_value('{name:John White, time:4:45,}','time') ----> '4:45'
    """

    after = after_first(s, keyword)
    before = before_first(after, ',')
    return before[before.index(':')+ 1:]
