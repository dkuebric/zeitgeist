API_KEY = 'your-api-key-here'

from collections import defaultdict
from github import Github
from stemming.porter2 import stem

g = Github(API_KEY)
r = g.get_repo('tracelytics/tracelons')

# word frequency!
words = defaultdict(int)

def add_words(d, text):
    if not text:
        return
    for w in text.lower().strip().split(' '):
        d[stem(w.strip())] += 1

open_issues = r.get_issues()
opens = defaultdict(int)
for i in open_issues:
    creator = i.user.login or 'none'
    opens[creator] += 1
    add_words(words, i.title)
    add_words(words, i.body)

closed_issues = r.get_issues(state='closed')
closes = defaultdict(int)
for i in closed_issues:
    creator = i.user.login or 'none'
    opens[creator] += 1
    closer = i.closed_by.login if i.closed_by else 'none'
    closes[closer] += 1
    add_words(words, i.title)
    add_words(words, i.body)

print "Issues Opened"
for (k,v) in opens.iteritems():
    print k, v

print
print "Issues Closed"
for (k,v) in closes.iteritems():
    print k, v

print
print "Sorted Words"
for w in sorted(words, key=words.get):
    print w.encode('ascii', 'ignore'),words[w]
