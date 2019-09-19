
import helpers


def removeLinesThatAreNotSentences(sentence):
     # if the sentences don't any have alphabets or numbers remove them
    import re
    if not re.search('[a-zA-Z0-9]', sentence):
        pass
    else:
        return sentence


def markComments(sentence, commentMarkerPrefix, commentMarkerSuffix):
    commentIndicators = helpers.commentIndicators
    if sentence:

        try:
            firstWord = isinstance(sentence[0], basestring)

        except ValueError:
            print('Input is not a word')
        else:
            if any(commentMarker in sentence[0] for commentMarker in commentIndicators):
                sentence.insert(0, commentMarkerPrefix)
                sentence.insert(len(sentence), commentMarkerSuffix)
                return sentence

            return sentence


def convertSentenceToListOfStrings(sentence):
    try:
        sentence
    except ValueError:
        print('The file is empty')
    else:
        sentence = removeLinesThatAreNotSentences(sentence)

        if sentence:
            return sentence.lstrip().lstrip('- ').rstrip(' -').split()


def getTimeCodes(sentence):

    if sentence:
        timeCodes = set()

        for word in sentence:
            if not helpers.isTimeCode(word):
                continue
            else:
                timeCodes.add(str(word))

        return timeCodes


def removeTimeCodes(sentence):

    if sentence:
        timeCodes = getTimeCodes(sentence)

        if timeCodes:
            sentence = [i for j, i in enumerate(
                sentence) if j in timeCodes]

            TimeCodesRemoved = filter(lambda a: a != '-', sentence)

            if TimeCodesRemoved:
                return TimeCodesRemoved

        return sentence


def removeSpeakers(sentence):
    if sentence:
        speakers = filter(lambda x: ':' in x, sentence)
        if speakers:
            for speaker in speakers:
                sentence = sentence[sentence.index(speaker)+1:]
                if sentence:
                    return sentence

        return sentence


def joinListOfStrings(stringList):
    try:
        if stringList:
            isinstance(stringList, list)
            all(isinstance(item, str) for item in stringList)
    except ValueError:
        print('excepted an array of strings')
    else:
        if stringList:
            return ' '.join(stringList)


def cleanScript(sentence):

    listOfStrings = convertSentenceToListOfStrings(sentence)
    TimeCodesRemoved = removeTimeCodes(listOfStrings)
    speakersRemoved = removeSpeakers(TimeCodesRemoved)
    finalList = markComments(speakersRemoved, '[', ']')
    sentence = joinListOfStrings(finalList)
    return sentence
