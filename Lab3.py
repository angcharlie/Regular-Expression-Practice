"""
 Charlie Ang
 CSC 4800 Python Applications Programming
 Lab # 3
 Dr. Tindall
 January 24, 2017

 This program tests regular expressions for the following Chapter 1 exercises
"""

import re
from RETest import testre


def exercise4():
    """
    Exercise 1-4
    Match the set of all valid Python identifiers.

    From language definition in the Python documentation:
    The valid characters for identifiers are: the uppercase and lowercase letters A through Z, the underscore _
    and, except for the first character, the digits 0 through 9.
    identifier ::=  (letter|"_") (letter | digit | "_")*
    :return:
    """

    print("Test Exercise 1-4")
    patt = r'''(
        ^[^\d\W]        # starts with: '^' inside [] means do not match any digit or non alphanumeric
        \w*             # followed by alphanumeric characters [A-Za-z0-9_] 0 or more times
        $               # match end of string (or \Z)
        )'''
    print("Pattern: '{}'".format(patt))

    # should match
    testre(patt, 'L')
    testre(patt, 'l')
    testre(patt, 'Ll9ervs_9284fex')
    testre(patt, '_')
    testre(patt, '_3')
    testre(patt, '_Llekjlkja283msdf')

    # should  not match
    testre(patt, '9')
    testre(patt, '9Ll_')
    testre(patt, '!@$')
    testre(patt, 'aa bb')
    testre(patt, '')
    print()


def exercise5():
    """
    Exercise 1-5
    Match a street address according to the American format.
    Keeps regular expression general enough to match any number of street words of multi-word street names
    1-5 digit number followed by 1 space, followed by 1 to N words separated by space
    :return:
    """

    print("Test Exercise 1-5")
    # 1-5 digits followed by space followed by 1 or more words separated by space
    patt = r'([0-9]{1,5}\s(\w\s*)+)'
    print("Pattern: '{}'".format(patt))

    # should match
    testre(patt, '3307 3rd')
    testre(patt, '3307 3rd West')
    testre(patt, '1180 Bordeaux Drive')
    testre(patt, '3210 De la Cruz Boulevard')
    testre(patt, '1 3rd West')
    testre(patt, '12345 Bordeaux Drive')

    # should  not match
    testre(patt, '123456 4th Ave')          # 6 digit house number
    testre(patt, '123')                     # no street name
    testre(patt, '')
    print()


def exercise6():
    """
    Exercise 1-6
    Match simple web domain names that begin with "www." and end with a ".com" suffix
    Valid domain names according to hscript.com: can have alphabets, numbers, and hyphens.
    Cannot begin or end with "-"
    :return:
    """

    print("Test Exercise 1-6")
    patt = r'(www\.[\w|\d][\w|\d|-]*[^-]\.com$)'
    print("Pattern: '{}'".format(patt))

    # should match
    testre(patt, 'www.google.com')
    #testre(patt, 'www.x.com')
    testre(patt, 'www.x-y-z.com')
    testre(patt, 'www.x---z.com')
    testre(patt, 'www.789abc.com')

    # should not match
    testre(patt, '')
    testre(patt, 'www.x----.com')
    testre(patt, 'www.-.com')
    testre(patt, 'www..com')
    testre(patt, 'www.-google.com')
    testre(patt, 'www.google-.com')
    testre(patt, 'www..com')
    testre(patt, 'www.spu.edu')
    testre(patt, 'www.abc.company')
    testre(patt, 'www.x.y.z.com')
    print()


def exercise7():
    """
    Exercise 1-7
    Match the set of the string representations of all Python integer literals.

    integer      ::=  decinteger | bininteger | octinteger | hexinteger
    decinteger   ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
    bininteger   ::=  "0" ("b" | "B") (["_"] bindigit)+
    octinteger   ::=  "0" ("o" | "O") (["_"] octdigit)+
    hexinteger   ::=  "0" ("x" | "X") (["_"] hexdigit)+
    nonzerodigit ::=  "1"..."9"
    digit        ::=  "0"..."9"
    bindigit     ::=  "0" | "1"
    octdigit     ::=  "0"..."7"
    hexdigit     ::=  digit | "a"..."f" | "A"..."F"
    :return:
    """
    print("Test Exercise 1-7")
    patt = r'''(
        \b              # start of number
        (?:             # choose one of following
        (?i)            # case-insensitive regex
        0x[0-9a-f]+ |   # hexinteger
        0o[0-7]+ |      # octinteger
        0b[01]+ |       # bininteger
        [1-9]\d* | 0+   # decinteger
        )
        \b              # end of number
        )'''
    print("Pattern: '{}'".format(patt))

    # should match
    testre(patt, '0x123456789abcdef')   # hex
    testre(patt, '0X123456789ABCDEF')   # hex
    testre(patt, '0o1234567')           # oct
    testre(patt, '0b010101010101010')   # binary
    testre(patt, '123224')              # dec
    testre(patt, '0')                   # ded
    testre(patt, '00000')               # dec

    # should not match
    testre(patt, '01')
    testre(patt, '0x123456789ABCDEFy')  # hex
    testre(patt, '0oabc1234567')        # oct
    testre(patt, '0O8')                 # oct
    testre(patt, '0b01010101320101010') # binary
    testre(patt, '0b12345')             # dec
    print()


def exercise11():
    """
    Exercise 1-11
    Match the set of all valid e-mail addresses
    :return:
    """

    print("Test Exercise 1-11")
    patt = r'[\w+|\w+\.]+@(\w+\.)*\w+\.[\w]{2,6}$'
    print("Pattern: '{}'".format(patt))

    # should match
    testre(patt, 'mht@spu.edu')
    testre(patt, 'a.b@c.com')
    testre(patt, 'Fred.H.Flintstone@bedrock.com')
    testre(patt, 'Fred.H.Flintstone@bedrock.us')
    testre(patt, 'Fred.H.Flintstone@bedrock.info')
    testre(patt, 'mht@cs.spu.edu')

    # should not match
    testre(patt, '')
    testre(patt, 'lkfjalksdf.com')
    testre(patt, '@.com')
    testre(patt, 'Fred.H.Flintstone@bedrock.infoiuyt')
    print()


def exercise12():
    """
    Exercise 1-12
    Match the set of all valid Web site addresses (URLs)
    :return:
    """

    print("Test Exercise 1-12")
    # begins with http:// and ends with 2-6 letter word (.com, .org, .us, etc.)
    patt = r'^http://www\.[\w|\d][\w|\d|-]*[^-]\.[\w]{2,6}$'
    print("Pattern: '{}'".format(patt))

    # should match
    testre(patt, 'http://www.google.com')
    testre(patt, 'http://www.789abc.com')
    testre(patt, 'http://www.789abc.us')
    testre(patt, 'http://www.789abc.org')
    testre(patt, 'http://www.789abc.asdfgh')

    # should not match
    testre(patt, '')
    testre(patt, 'http://www.x---.com')
    testre(patt, 'htp://www.google.com')
    testre(patt, 'www.google.com')
    testre(patt, 'http://www.google.company')
    print()


def main():
    """
    Calls each exercise to run unit testing on its regular expression
    :return:
    """

    exercise4()                              # Exercise 1-4
    exercise5()                              # Exercise 1-5
    exercise6()                              # Exercise 1-6
    exercise7()                              # Exercise 1-7
    exercise11()                             # Exercise 1-11
    exercise12()                             # Exercise 1-12

if __name__ == '__main__':
        main()

