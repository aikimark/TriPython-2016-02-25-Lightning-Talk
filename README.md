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
stopwords|0.001045|0.001064|0.001052|0.001272
stopwordsbyfreq|0.000912|0.001272|0.000957|0.002249
stopwordsDic|0.000462|0.000500|0.000505|0.000590
stopwordsInlist|0.000836|0.000968|0.000886|0.002135
stopwordsSet|0.000420|0.000654|0.000462|0.001750

### The performance winners are: ###
1. Set
2. Dictionary
3. Binary search
4. list ordered by expected occurance (frequency)
5. a list in any order
