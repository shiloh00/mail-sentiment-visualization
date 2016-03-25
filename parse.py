import mailbox
import pickle
from email.header import decode_header
results = []
m = {'english':0}
for message in mailbox.mbox('gmail.mbox'):
    #print message.keys()
    subject = message['subject']# Could possibly be None.
    pair = decode_header(subject)[0]
    k = pair[1]
    if k:
        if k in m:
            m[k] = m[k] + 1
        else:
            m[k] = 1
    else:
        m['english'] = m['english'] + 1
        results.append({'subject':message['subject'],'from':message['from'], 'date':message['date']})

with open('english.pkl', 'wb') as fp:
    pickle.dump(results, fp)
print m
    
