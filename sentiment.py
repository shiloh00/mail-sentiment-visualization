import pickle
import json
import subprocess
from textblob import TextBlob
res = pickle.load(open('divided_month.pkl'))
m = {}
p = {}
pos = 0
neg = 0
neu = 0

for key, value in res.iteritems():
    m[key] = {'pos':0, 'neg':0, 'neutral':0} 
    for n in value:
        tmp =  n['subject']
        try:
            text = TextBlob(tmp)
            if  text.sentiment.polarity == 0:
                m[key]['neutral'] = m[key]['neutral'] + 1
            elif text.sentiment.polarity > 0:
                m[key]['pos'] = m[key]['pos'] + 1
            else:
                m[key]['neg'] = m[key]['neg'] + 1
        except:
            pass
with open('stat.json', 'wb') as fp:
    json.dump(m, fp)
print m
