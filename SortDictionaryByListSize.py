#-------------------------------------------------------------------------------
# Name:        Lightning Talk Code, part 1
# Purpose:
#   * Show the solution to an interesting EE problem: http://rdsrc.us/ZruKyU
#   * Problem is to find the minimum covering set of words used in a set of
#     sentences.  What is the smallest set of words that would appear in one
#     or more sentences, such that all the sentences are 'represented'.
#     https://en.wikipedia.org/wiki/Covering_problems
#   * Show the sorting of dictionary by the length of the list (value) of
#     each dictionary item.
#   * Show the use of the itertools library's combinations method
#
# Author:      Mark Hutchinson
#
# Created:     2016-02-25
# Copyright:   (c) Mark Hutchinson 2016
#-------------------------------------------------------------------------------
import itertools

def main():
    dicWords = {}
    stopwords=['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']
    slist = ["Expert exchange is a nice site", "There are few sites like expert exchange",
            "google is a search engine", "i can search for anything", "cold day"]

    #populate dicWords dictionary with the non-stop words and list of their sentence indexes
    for posn, sentence in enumerate(slist):
        for w in sentence.lower().split(" "):
          if w not in stopwords:
            if dicWords.has_key(w):
                dicWords[w].append(posn)
            else:
                dicWords[w]= [posn]
    print "===============\ndicWords:\n\t", dicWords      #not necessary, but useful to see the results of the sentences/words iterations

    #sort dictionary by list length
    dicFreqWords = sorted(dicWords, key=lambda l: len(dicWords[l]), reverse=True)

    #====================================================
    #ToDo: eliminate all but first (occurance) words with duplicate sentence sets
    #====================================================

    #also not necessary, but useful to see the results of the dictionary sort operation
    print "===============\ndicFreqWords (word and sentence index list):"
    for dword in dicFreqWords:
        print "\t", dword, dicWords[dword]

    coveringset = [f for f in xrange(len(slist))]
    bFound=False
    for csWordCount in coveringset[1:]:
        if bFound:
            break
        for combinationset in itertools.combinations(dicFreqWords, csWordCount):
            cs = []   #covering set variable for this combination
            for dWord in [dicWords[x] for x in combinationset]:
                cs+= dWord
            if set(cs) == set(coveringset):
                print "=============\nFound: ", cs, combinationset
                bFound = True
                break

    #====================================================
    #ToDo: handle the case that bFound = False
    #====================================================

if __name__ == '__main__':
    main()