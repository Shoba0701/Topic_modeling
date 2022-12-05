from random import random
import snscrape.modules.twitter as sntwitter
import pandas as pd
from openpyxl.workbook import Workbook
import random

start_time = time.time()

# key_words = ["traffic","accident","poverty","scarcity","pollution","crime","theft","bribery","abuse","racism"]
key_words = ["accident","child abuse","bribery","theft","racism","floods","drug acciction","poverty","terrorism","medical emergency"]
# random_num = random.sample(range(1000,5000),10)

all_tweets=[]

for idx,i in enumerate(key_words):
    qurey ='"{}" lang:en until:2022-09-30 since:2022-09-01'.format(i)
    limit = 1000
    
    tweets =[]

    for tweet in sntwitter.TwitterSearchScraper(qurey).get_items():
        # print(vars(tweet))
        # break
        if len(tweets) == limit:
            break
        else:
            tweets.append([str(tweet.date),tweet.user.username,tweet.content]) 
        
    df = pd.DataFrame(tweets,columns=["date","username","content"])
    df["key"] = i
    
    all_tweets.append(df)    
df_new =pd.concat(all_tweets)    
    
df_new.to_excel("data_with_keywords_set_3_equal_datapoints.xlsx")  


end_time = time.time()
print(f"Time taken to extract data is {(end_time-start_time)/60} minutes")

