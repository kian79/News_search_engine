#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from collections import Counter
import re


# In[2]:


DATA_PATH = ''


# In[33]:


extra_data = pd.read_csv(DATA_PATH+'extra_data.csv')
punctuations = extra_data['punctuations'].dropna().to_list()
stop_words = extra_data['stop_words'].dropna().to_list()
suffix_u = extra_data['suffix_u'].dropna().to_list()
suffix = extra_data['suffix'].dropna().to_list()
ar = extra_data['ar'].dropna().to_list()
pr = extra_data['pr'].dropna().to_list()
verb_post = extra_data['verb_post'].dropna().to_list()
verb_pre = extra_data['verb_pre'].dropna().to_list()
verbs = extra_data['verbs'].dropna().to_list()
df = pd.read_csv(DATA_PATH+'IR_data.csv')
mokasar = pd.read_csv(DATA_PATH+'mokasar.csv')
df


# In[24]:


mokasar = mokasar.set_index('jam').T.to_dict('dict')


# In[25]:


suffix


# In[39]:


df = df.dropna()


# In[27]:


def tokenize(text):
  tokens = set([word for word in text.split()])
  return tokens


# In[28]:


def delete_suffix(word, suffix,u=1):
  word_end = word.index(suffix[0])
  if u and '\u200c' in word and word.index('\u200c') == word_end - 1 and word.endswith(suffix):
    word = word[:word_end-1]
  elif not u and suffix in word and word.replace(suffix,'') in all_words and word.endswith(suffix):
    if suffix == 'گان':
      word = word.replace(suffix,'ه')
    else:
      word = word.replace(suffix,'')
  return word


# In[29]:


def delete_punctuations(word):
  for punc in punctuations:
    if punc in word:
      word = word.replace(punc," ")
  return word


# In[52]:


def delete_none_words(word):
    persian_pattern =  "^[\u0643\u0623\u0629\u0624\u0621\u0626\u0622\u0627\u0628\u067E\u062A-\u062C\u0686\u062D-\u0632\u0698\u0633-\u063A\u0641\u0642\u06A9\u06AF\u0644-\u0648\u06CC]+$"
    if re.match(persian_pattern,word):
        return word
    return ""


# In[53]:


def normalize_letters(word):
    for i in len(ar):
        if ar[i] in word:
            word.replace(ar[i],pr[i])


# In[102]:


delete_none_words(w)


# In[100]:


w


# In[54]:


def normalize_mokasar(word):
    if word in mokasar.keys():
        word = mokasar[word]['mofrad']
    return word


# In[64]:


def normalize_verb(verb):
    for v in verbs:
        if verb in v:
            for p in verb_pre:
                if verb.startswith(p):
                    verb = verb.replace(p,'')
            for p in verb_post:
                if verb.endswith(p):
                    verb = verb.replace(p,'')
    return verb


# In[56]:


text_list = df.content.to_list()
all_words = tokenize(" ".join(text_list))
# for i in range(len(all_words)):
#     all_words[i] = delete_none_words(all_words[i])
all_words = [delete_none_words(a_w) for a_w in all_words if delete_none_words(a_w)]


# In[57]:


len(all_words)


# In[58]:


words_freq = dict(Counter(all_words))


# In[59]:


len(words_freq)


# In[71]:


from tqdm import tqdm


# In[72]:


def normalize_words(text_list):
  words_dict = {}
  for i in tqdm(range(len(text_list))):
    temp_words = text_list[i].split()
    temp_words = [w.strip() for w in temp_words if w.strip() not in stop_words]
    
    # print
    # for word in text_list[i].split():
    #   if word in stop_words:
    #     word = ""
    x = temp_words
    for j in range(len(temp_words)):
      temp_words[j] = delete_punctuations(temp_words[j])
      temp_words[j] = delete_non_words(temp_words[j])
      temp_words[j] = normalize_verb(temp_words[j])
      for s in suffix_u:
        if s in temp_words[j]:
          temp_words[j] = delete_suffix(temp_words[j],s)
          break
      for s in suffix:
        if s in temp_words[j]:
          temp_words[j] = delete_suffix(temp_words[j],s,u=0)
          break
    temp_words = [w for w in temp_words if w.strip() not in stop_words]

    words = list(map(str.strip, temp_words))
    for j in range(len(words)):
      if words[j] not in words_dict.keys():
        words_dict[words[j]] = {}
      if i not in words_dict[words[j]].keys():
        words_dict[words[j]][i] = 1
      else:
        words_dict[words[j]][i] += 1
  return words_dict


# In[73]:


indexed_words = normalize_words(text_list)


# In[75]:


del indexed_words['']


# In[76]:


len(indexed_words)


# In[77]:


for k in indexed_words.keys():
    if len(k) < 3:
        print(k)


# In[78]:


indexed_words['ج']


# In[82]:


a = [text_list[40]]


# In[83]:


text_list[40]


# In[84]:


x = normalize_words(a)


# In[85]:


x


# In[89]:


query = 'واکسیناسیون بیماری کرونا در ایران'


# In[90]:


query = normalize_words([query])


# In[91]:


query


# In[124]:


match = []
for q in query.keys():
    for iw in indexed_words.keys():
        if q == iw:
            print(iw)
            match.append(list(indexed_words[iw].keys()))
            print(len(match))
#     return match


# In[125]:


len(match)


# In[128]:


def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3


# In[129]:


mm = match[0]
for m in match:
    mm = intersection(mm,m)


# In[130]:


mm


# In[131]:


text_list[5589]


# In[101]:


w = 'ایران'
for s in suffix_u:
    if s in w:
        print(s)
        print(1,w)
        w = delete_suffix(w,s)
        print(2,w)
for s in suffix:
    if s in w:
        print(s)
        print(3,w)
        w = delete_suffix(w,s,u=0)
        print(4,w)


# In[57]:


w = 'ایران'
w.endswith('ان')


# In[103]:


normalize_words([w])


# In[98]:


flag = True
for text in text_list:
    t = list(text.split())
    for w in range(len(t)):
        if t[w] == 'ار':
            print(w)
            a = text
            print(text)
            flag = False
            break
    if not flag:
        break


# In[78]:


a.split()[570]


# In[133]:


delete_punctuations('۲۶')


# In[130]:





# In[139]:


bool(re.match("^[\u0600-\u06FF]+$", '123'))


# In[146]:


bool(re.match("^[آ-ی]$",'پس'))


# In[177]:


bool(re.match(pat, 'رئیسی'))


# In[159]:


'۷'.encode()


# In[161]:


'\u0622'


# In[170]:


'آ'.encode()

