import pandas as pd

new_df = pd.read_csv('/Users/sachinsinghal/Downloads/590_Unstructured/Appliances_title_topic_lda.csv')

out=[]

for i in new_df['title']:
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

new_df['title']=out

list_appliances = ['oven', 'conditioner', 'dryer', 'refrigerator', 'microwave', 'cooktop', 'coffee']



res={}
for_model = []
for i in out:
    for item in list_appliances:
        if (item in i.lower()):
            res[i]=item
            for_model.append(i)
df = pd.DataFrame.from_dict(res,orient = 'index')
df.rename(columns={0: "Topic"},inplace=True)
df.index.names = ['Title']
df.to_csv('/Users/sachinsinghal/Downloads/590_Unstructured/appliances_categories.csv')

remaining = []
for i in out:
    if i not in for_model:
        remaining.append(i)

train_furniture = df.index
test_furniture = df.Topic

## TFIDF Vectorization
from sklearn.feature_extraction.text import TfidfVectorizer
 # Trick: create a dummy tokenizer
def tk(doc): return doc
vec = TfidfVectorizer(analyzer='word',tokenizer=tk, preprocessor=tk,token_pattern=None,
min_df=2, ngram_range=(1,2), stop_words='english')
vec.fit(train_furniture)
training_x_furniture = vec.transform(train_furniture)
remaining_furniture = vec.transform(remaining)

# testing_x = vec.transform(test_furniture)

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(training_x_furniture,test_furniture,test_size = 0.2)

## Logit
from sklearn.linear_model import LogisticRegression
Logitmodel = LogisticRegression()
# training
Logitmodel.fit(X_train, y_train)
y_pred_logit = Logitmodel.predict(X_test)
 # evaluation
from sklearn.metrics import accuracy_score
acc_logit = accuracy_score(y_test, y_pred_logit)
print("Logit model Accuracy:: {:.2f}%".format(acc_logit*100))

y_pred_logit = Logitmodel.predict(remaining_furniture).tolist()

final_result = pd.DataFrame(
    {'Title': remaining,
     'Topic': y_pred_logit
    })

final_result.to_csv('/Users/sachinsinghal/Downloads/590_Unstructured/appliances_logistic.csv')



 ## Naive Bayes
from sklearn.naive_bayes import MultinomialNB
NBmodel = MultinomialNB()
# training
NBmodel.fit(X_train, y_train)
y_pred_NB = NBmodel.predict(X_test)
# evaluation
acc_NB = accuracy_score(y_test, y_pred_NB)
print("Naive Bayes model Accuracy:: {:.2f}%".format(acc_NB*100))

## SVM
from sklearn.svm import LinearSVC
SVMmodel = LinearSVC()
# training
SVMmodel.fit(X_train, y_train)
y_pred_SVM = SVMmodel.predict(X_test)
# evaluation
acc_SVM = accuracy_score(y_test, y_pred_SVM)
print("SVM model Accuracy: {:.2f}%".format(acc_SVM*100))

y_pred_svm = Logitmodel.predict(remaining_furniture).tolist()

final_result = pd.DataFrame(
    {'Title': remaining,
     'Topic': y_pred_svm
    })

final_result.to_csv('/Users/sachinsinghal/Downloads/590_Unstructured/appliances_svm.csv')


## decision tree and random forest
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

DTmodel = DecisionTreeClassifier()
RFmodel = RandomForestClassifier(n_estimators=550, max_depth=3, bootstrap=True,random_state=0)  ## number of trees and number of layers/depth
# training
DTmodel.fit(X_train, y_train)
y_pred_DT = DTmodel.predict(X_test)
RFmodel.fit(X_train, y_train)
y_pred_RF = RFmodel.predict(X_test)
# evaluation
acc_DT = accuracy_score(y_test, y_pred_DT)
print("Decision Tree Model Accuracy: {:.2f}%".format(acc_DT * 100))
acc_RF = accuracy_score(y_test, y_pred_RF)
print("Random Forest Model Accuracy: {:.2f}%".format(acc_RF * 100))




