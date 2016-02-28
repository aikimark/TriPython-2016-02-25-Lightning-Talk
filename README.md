# TriPython-2016-02-25-Lightning-Talk #

## Part 1: ##
* Show covering set problem solution using itertools
* Show sorting of dictionary by length of the values

## Part2: ##
* Show timings of different set inclusion/exclusion operations

### Timing Results ###
I ran the code a couple of dozen times.

Method|Min|Avg|Median|Max
------|---|---|------|---
stopwords|0.001056|0.001084|0.001061|0.001275
stopwordsbyfreq|0.000904|0.000925|0.000910|0.001007
stopwordsDic|0.000461|0.000467|0.000464|0.000541
stopwordsInlist|0.000855|0.000889|0.000865|0.001205

### The performance winners are: ###
1. Dictionary
2. Binary search
3. list ordered by expected occurance (frequency)
4. a list in any order
