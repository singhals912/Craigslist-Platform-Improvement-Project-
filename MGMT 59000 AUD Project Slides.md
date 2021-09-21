

Curious | Clusters

MGMT 59000 AUD

Craigslist

Platform

Improvement

Project

Cluster Centers -

Ø Pulkit Batra

Ø Esha Kaushal

Ø Laura Rossi

Ø Sachin Singhal

Ø Abhinav Reddy Vangala





Curious | Clusters

Background

• Craigslist (stylized as craigslist) is an American classified

advertisements website

• The craigslist platform is advertiser oriented, providing a simple, low-

structure interface where advertisers can create their ads with few

constraints.

• However, this low-structure creates additional work for potential buyers

who have to parse through the content to find what they need.





Curious | Clusters

Business Analysis

Current State

3 tier classification system :

Cons:

X Irrelevant results

• Example:

NYC

Location

X Inability to refine searches

X Not at par with competitors

• Example:

For sale

Category

•Examples:

Clothing,

Appliances,

Electronics

Subcategory





Curious | Clusters

Business Analysis

Our Solution

4th tier of categorization

• Users can refine search res

• No additional effort on behalf of advertisers

• Categories are always relevant to advertised

products





Curious | Clusters

Data Analysis

1

Data Acquisition

2

Data Cleaning

3

Topic Modeling

White

space

Lemmatization

Punctuation

Capitalization

Vectorization





Curious | Clusters

Data Analysis

Topics to Categories

5

Classification

6

Implementation

4

T1 1 2 3 4 …

T2 1 2 3 4 …

T3 1 2 3 4 …

T4 1 2 3 4 …

T5 1 2 3 4 …

T6 1 2 3 4 …





Curious | Clusters

Classification Process

Craigslist Ads title dataset

Final Labelled Dataset

S.N Title

o

Label

S.No

Title

1

Two Cutter & Buck

menâ€™s shirts, size

XL…..

Manual intervention to

merge similar topics

Topics

1

2

3

4

5

Two Cutter & Buck menâ€™s Shirt

shirts, size XL…..

LDA

Shirt

Suit

Sleeve

Shoe

Sandal

Men's Wool Dress Suit Pin

Stripes, 33 wai….

Dress

2

3

4

5

Men's Wool Suit Pin

Stripes, 33 wai….

Dress

Selling a pair of shoes that…. Footw

ear

Selling a pair of shoes

that….

Footwear

3 Menâ€™s size 15 1/2 short Dress

sleeve……

3 Menâ€™s size 15 1/2

short sleeve……

Real snake Sandals…….

Footw

ear

Real snake Sandals…….





Curious | Clusters

Validation

Furniture

Classification

Appliances

Classification

Clothing and

Accessories

classification

SVM

SVM

98.48%

96.88%

99.62%

98.60%

99.9%

Naïve

Bayes

Logistic

Regression

99.04%

Decision Tree

Naïve Bayes

94.48%

79.17%

66.69%

97.96%

90.57%

81.53%

95.49%

87.52%

80.33%

Random Forest





Curious | Clusters

Value add for Business

No

additional

work

required of

advertisers

Single, one

time topic

selection.

Simplify

search for

buyer

Improved

User

Experience





Curious | Clusters

Conclusion

Simple algorithm provides easy

classification

Some manual intervention required in

selecting best topics

Room to grow into more categories





Curious | Clusters

Thank you

