#-------------------------------------------------------------------------------
# Name:        Lightning Talk Code, part 2
# Purpose:
#   * Show different methods and data structures for looking for
#     list inclusion/exclusion.
#   * Introduce the bisect library
#   * Show timing results and give recommendations
# Author:      Mark Hutchinson
#
# Created:     2016-02-25
# Copyright:   (c) Mark Hutchinson 2016
#-------------------------------------------------------------------------------
import timeit
import bisect

#inlist is a binary search function using the bisect_left method
def inlist(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    else:
        return False

def main():
    #stopwords are the (English) stop words in alphabetic order
    stopwords = ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by','can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers','him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my','neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so','some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what','when','where','which','while','who','whom','why','will','with','would','yet','you','your']
    #stopwordsbyfreq are the (English) stop words in sorted in descending word use order
    stopwordsbyfreq = ['the','of','and','a','to','in','is','be','that','was','he','for','it','with','as','his','i','on','have','at','by','not','they','this','had','are','but','from','or','she','an','which','you','we','all','were','her','would','there','their','will','when','who','him','been','has','if','no','do','so','can','what','said','about','other','into','than','its','only','could','them','some','these','then','may','any','like','my','our','most','me','after','also','did','must','where','get','your','should','because','just','say','how','own','too','us','while','might','off','since','however','does','got','every','almost','let','yet','why','rather','among','often','ever','least','am','either','cannot','across','able','says','nor','else','likely','neither','whom','wants','dear','hers','tis','twas']
    #stopwordsDic are the (English) stop words in a dictionary
    stopwordsDic = {'a' : 1,'able' : 1,'about' : 1,'across' : 1,'after' : 1,'all' : 1,'almost' : 1,'also' : 1,'am' : 1,'among' : 1,'an' : 1,'and' : 1,'any' : 1,'are' : 1,'as' : 1,'at' : 1,'be' : 1,'because' : 1,'been' : 1,'but' : 1,'by' : 1,'can' : 1,'cannot' : 1,'could' : 1,'dear' : 1,'did' : 1,'do' : 1,'does' : 1,'either' : 1,'else' : 1,'ever' : 1,'every' : 1,'for' : 1,'from' : 1,'get' : 1,'got' : 1,'had' : 1,'has' : 1,'have' : 1,'he' : 1,'her' : 1,'hers' : 1,'him' : 1,'his' : 1,'how' : 1,'however' : 1,'i' : 1,'if' : 1,'in' : 1,'into' : 1,'is' : 1,'it' : 1,'its' : 1,'just' : 1,'least' : 1,'let' : 1,'like' : 1,'likely' : 1,'may' : 1,'me' : 1,'might' : 1,'most' : 1,'must' : 1,'my' : 1,'neither' : 1,'no' : 1,'nor' : 1,'not' : 1,'of' : 1,'off' : 1,'often' : 1,'on' : 1,'only' : 1,'or' : 1,'other' : 1,'our' : 1,'own' : 1,'rather' : 1,'said' : 1,'say' : 1,'says' : 1,'she' : 1,'should' : 1,'since' : 1,'so' : 1,'some' : 1,'than' : 1,'that' : 1,'the' : 1,'their' : 1,'them' : 1,'then' : 1,'there' : 1,'these' : 1,'they' : 1,'this' : 1,'tis' : 1,'to' : 1,'too' : 1,'twas' : 1,'us' : 1,'wants' : 1,'was' : 1,'we' : 1,'were' : 1,'what' : 1,'when' : 1,'where' : 1,'which' : 1,'while' : 1,'who' : 1,'whom' : 1,'why' : 1,'will' : 1,'with' : 1,'would' : 1,'yet' : 1,'you' : 1,'your' : 1}

#    f=file("c:\users\mark\documents\GettysburgAddress.txt",'r')
    f=file(".\GettysburgAddress.txt",'r')
    lines= f.readlines()
    f.close()

    #do some clean-up of the text
    for m in range(3):
        lines[m] = lines[m].lower().replace(".","").replace(",","").replace("\n","")

    nfcount=0
    methodtime=0
    for line in lines:
        for word in line.split(" "):
            start = timeit.default_timer()
            if word not in stopwords:
                nfcount += 1
            methodtime += timeit.default_timer() - start
    print "stopwords\t", methodtime, "\t", nfcount

    nfcount=0
    methodtime=0
    for line in lines:
        for word in line.split(" "):
            start = timeit.default_timer()
            if word not in stopwordsbyfreq:
                nfcount += 1
            methodtime += timeit.default_timer() - start
    print "stopwordsbyfreq\t", methodtime, "\t", nfcount

    nfcount=0
    methodtime=0
    for line in lines:
        for word in line.split(" "):
            start = timeit.default_timer()
            if not stopwordsDic.has_key(word):
                nfcount += 1
            methodtime += timeit.default_timer() - start
    print "stopwordsDic\t", methodtime, "\t", nfcount

    nfcount=0
    methodtime=0
    for line in lines:
        for word in line.split(" "):
            start = timeit.default_timer()
            if not inlist(stopwords, word):
                nfcount += 1
            methodtime += timeit.default_timer() - start
    print "stopwordsInlist\t", methodtime, "\t", nfcount

if __name__ == '__main__':
    main()
