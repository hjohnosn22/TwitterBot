#Henry Johnson
#The function of this program is to hold extra functions that are not used in main.py
#date created 12/7/20
#last edited 12/14/20


#retrieves last tweet in you homeline
timeline = api.home_timeline()

for tweet in timeline:
    print(f"{tweet.user.name} said {tweet.text}")
#*********************************************************
#This will right a tweet
api.update_status("Test tweet from Tweepy Python")
#************************************************
#This will print a users details
user = api.get_user("revanth1001")

print("User details:")
print(user.name)
print(user.description)
print(user.location)

print("Last 20 Followers:")

for follower in user.followers():
    print(follower.name)
#*************************************
#this will search twitter for certain key words
for tweet in api.search(q="Python", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")
#********************************************
#this method will stream tweets that match certain criteria

#*************************************************
#writes into a text file
f = open("<TextFile>", "a")
f.write("Now the file has more content!")
f.close()