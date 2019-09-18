
import helpers


def removeExtras(sentence):
     # if the sentences dont any have alphabets or numbers remove them
    import re
    if not re.search('[a-zA-Z0-9]', sentence):
        pass
    else:
        return sentence


def markComments(sentence, commentMarkerPrefix, commentMarkerSuffix):

    commentIndicators = ['//',
                         '/',
                         '#',
                         '*',
                         '(',
                         '--',
                         '-->',
                         '%', ]
    if sentence:

        try:
            firstWord = isinstance(sentence[0], basestring)

        except ValueError:
            print('Input is not a word')
        else:
            if any(prefix in sentence[0] for prefix in commentIndicators):
                sentence.insert(0, commentMarkerPrefix)
                sentence.insert(len(sentence), commentMarkerSuffix)
                return sentence

            return sentence


def splitSentences(text):
    try:
        text
    except ValueError:
        print('The file is empty')
    else:
        sentence = removeExtras(text)
        if sentence:
            return sentence.lstrip().lstrip('- ').rstrip(' -').split()


def getTimeCodes(sentence):

    import helpers
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


def joinArrayOfWords(Array):
    try:
        if Array:
            isinstance(Array, list)
            all(isinstance(item, str) for item in Array)
    except ValueError:
        print('excepted an array of strings')
    else:
        if Array:
            return ' '.join(Array)


def cleanScript(sentence):

    sentence = splitSentences(sentence)
    TimeCodesRemoved = removeTimeCodes(sentence)
    speakersRemoved = removeSpeakers(TimeCodesRemoved)
    final = markComments(speakersRemoved, '[', ']')
    joined = joinArrayOfWords(final)
    return joined
