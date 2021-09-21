import pandas as pd
# df = pd.read_json('/Users/sachinsinghal/PycharmProjects/pythonProject/BookScraping/BookScraping/Craiglist/finals.json')
# df.to_csv('/Users/sachinsinghal/PycharmProjects/pythonProject/BookScraping/BookScraping/Craiglist/new.csv',index=False)

new_df = pd.read_csv('/Users/sachinsinghal/Downloads/results-furniture_clean_all.csv')

out=[]

for i in new_df['Title']:
    k=i.strip()
    k = " ".join(k.split())
    k = k.replace('\\n', '')
    k = k.replace('[', '')
    k = k.replace(']', '')
    k = k.replace(',', '')
    k = k.replace("'", '')
    k = k.replace('"', '')
    k=k.strip()
    out.append(k)

new_df['Title']=out

new_df.to_csv('/Users/sachinsinghal/Downloads/590_Unstructured/Final.csv',index=False)

from PIL import Image
from pylab import *
import pandas as pd
import matplotlib.pyplot as plt
import glob
import nltk


#Answer 2
#
# reviews=pd.read_excel('/Users/sachinsinghal/Downloads/590_Unstructured/Assignment 2 text.xlsx',sheet_name=0)
# reviews.head(2)

review_doc = []
for i in new_df['Title']:
    review_doc.append(i)

#Tokenzing each review using nltk.word_tokenize()
tokenized = []
for i in review_doc:
    tokenized.append(nltk.word_tokenize(str(i)))


lemmatizer = nltk.stem.WordNetLemmatizer()

#Lemmatizing each word provided it's alphabatical and converting it into lowercase
lemmatized_v1= []
for token in tokenized:
    lemmatized = []
    for i in token:
        if i.isalpha() and len(i)>2 and i not in ('maker','great','range'):
            lemmatized.append(lemmatizer.lemmatize(i.lower()))
    lemmatized_v1.append(lemmatized)


#converting retrieved words in step 3 in documents
POS_f2 = []
for i in lemmatized_v1:
    POS_f2.append(" ".join(i))

# def tk(review_doc):
#     return review_doc

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer2 = TfidfVectorizer(analyzer='word',min_df=10, ngram_range=(1,2), stop_words='english')
vectorizer2.fit(POS_f2)
print(vectorizer2.vocabulary_)
v2 = vectorizer2.transform(POS_f2)
print(v2.toarray())
p3= v2.toarray()
# new_df=pd.DataFrame(p3)
# new_df.to_csv('/Users/sachinsinghal/Downloads/590_Unstructured/image/Ans_3_dummy.csv')

terms = vectorizer2.get_feature_names()
from sklearn.decomposition import LatentDirichletAllocation
lda = LatentDirichletAllocation(n_components= 20).fit(v2)

new_dict={}
for topic_idx, topic in enumerate(lda.components_):
    new_dict[topic_idx] = " ".join([terms[i] for i in topic.argsort()[:-1-2:-1]])
    print("Topic %d:" % (topic_idx))
    print(" ".join([terms[i] for i in topic.argsort()[:-1-2:-1]]))

top_6_topics=pd.DataFrame.from_dict(new_dict, orient='index')
headers = ['Topic Description']
top_6_topics.columns = headers
top_6_topics.index.names = ['Topic ID']
top_6_topics.to_csv('/Users/sachinsinghal/Downloads/590_Unstructured/image/topics_1.csv')

# from numpy import s_
# x=[v2[0:20],v2[501:511]]
# review_cut = [review_doc[0:20],review_doc[501:511]]

new_review_cut = [sublist for sublist in review_doc]


new_list = []
for i in v2:
    p = lda.transform(i)
    one_list= []
    for j in p:
        inner_list = []
        # print(j.argsort()[:-2-1:-1])
        topic_id = j.argsort()[:-1-2:-1]
        for i in topic_id:
            inner_list.append(new_dict[i])
            # print(new_dict[i])
        one_list.append(inner_list)
    new_list.append(one_list)

new_topic = [item for sublist in new_list for item in sublist]
sries_1 = pd.Series(new_topic, index =range(len(new_topic)))
sries_2 = pd.Series(new_review_cut, index =range(len(new_review_cut)))
final_df=pd.DataFrame({'title':new_review_cut, 'topic':new_topic})


# top10_10 =dict(zip(new_review_cut, new_topic))
# top_10_df=pd.DataFrame.from_dict(top10_10, orient='index')
# headers = ['Topic Priority 1','Topic Priority 2']
# top_10_df.columns = headers
# top_10_df.index.names = ['Review']
final_df.to_csv('/Users/sachinsinghal/Downloads/590_Unstructured/image/furniture_40.csv')


# count = 0
# for i in range(len(review_doc)):
#     if (review_doc[i]) == NaN:
#         count=count+1