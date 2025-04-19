def replaceowith0(text):

    firstoindex = text.find('о')
    lastoindex = text.rfind('о')


    result = text[:firstoindex + 1] + text[firstoindex + 1:lastoindex].replace('о', '0') + text[lastoindex:]

    return result