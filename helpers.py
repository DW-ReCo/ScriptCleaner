import time
from dateutil import parser


def isTimeCode(date):

    # Return whether the string can be interpreted as a date.

    # : param string: str, string to check for date
    # : param fuzzy: bool, ignore unknown tokens in string if True
    sepraters = ['-', '/', ':']
    for seprater in sepraters:
        if seprater in date:
            try:
                parser.parse(str(date), fuzzy=True)
                return True
            except ValueError:
                return False


commentIndicators = ['//',
                     '/',
                     '#',
                     '*',
                     '(',
                     '--',
                     '-->',
                     '%',
                     '[]']


commentMarker = {
    'squareBrackets': "[]"
}


def insertToList(sentence, marker):
    if isinstance(sentence, list):
        sentence.insert(0, marker[0])
        sentence.insert(len(sentence), marker[1])
        return sentence
