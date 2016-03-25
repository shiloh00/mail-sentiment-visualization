import pickle
import pprint
from dateutil.parser import parse
from datetime import datetime
res = pickle.load(open('english.pkl'))
m = {}
for message in res:
    n = {}
    b = parse(message['date'])
    month = str(b.year) + '-' + str(b.month)
    n['sender'] = message['from']
    n['subject'] = message['subject']
    if month in m:
        m[month].append(n)
    else:
        m[month] = [n]
with open('divided_month.pkl', 'wb') as fp:
    pickle.dump(m, fp)
    




