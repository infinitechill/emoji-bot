#! /usr/local/bin/python3
# infinite chill / 2017

import sys, time, random, emoji, tweepy

bugs = {"bug1" : ":bug:", "bug2" : ":beetle:", "bug3" : ":ant:", "bug4" : ":snail:"}
flying = {"flying1" : ":bee:"}
leafs = {"leaf1" : ":maple_leaf:", "leaf2" : ":fallen_leaf:", "leaf3" : ":leaves:"}
plants = {"plant1" : ":seedling:", "plant2" : ":hibiscus:", "plant3" : ":blossom:", "plant4" : ":cherry_blossom:", "plant5" : ":mushroom:", "plant6" : ":sunflower:"}


def get_random_emoji_tweet():
    myleafs = list(leafs.values())
    mybugs = list(bugs.values())
    myplants = list(plants.values())
    myflying = list(flying.values())
    result_string=""
    # vertical length of sky..
    last_used=""
    for i in range(5):
        count=0
        # width of scene
        for i in range(40):
            # 1/10 chance of printing an emoji, else print space
            todo=random.randint(0,10)
            if todo == 0:
                # 1/5 chance of printing an emoji from flying list, else print a leaf
                todo=random.randint(0,5)
                if todo == 0:
                    randomflyingindex=random.randint(0, len(flying)-1 )
                    result_string += emoji.emojize(myflying[randomflyingindex], use_aliases=True) + "  "
                    last_used=myflying[randomflyingindex]
                else:
                    randomleafindex=random.randint(0, len(myleafs)-1 )    
                    while( myleafs[randomleafindex] == last_used):
                        randomleafindex=random.randint(0, len(myleafs)-1 )
                    result_string += emoji.emojize(myleafs[randomleafindex], use_aliases=True) + "  "
                    last_used=myleafs[randomleafindex]
                count+=1               
            # no emoji, print a space...
            else:
                result_string += " "
            # if we have reached max emojis, pass
            if count == 3:
                break
        result_string += "\n"

    count=0
    for i in range(40):
        todo=random.randint(0,5)
        if todo == 0:
            randombugindex=random.randint(0, len(mybugs)-1 )
            while( mybugs[randombugindex] == last_used ):
                randombugindex=random.randint(0, len(mybugs)-1 )
            result_string += emoji.emojize(mybugs[randombugindex], use_aliases=True) + "  "
            last_used=mybugs[randombugindex]
            count+=1
        else:
            result_string += "  "
        if count == 3:
            break
    return result_string


def main():    
    CONSUMER_KEY = ' replace this... '
    CONSUMER_SECRET = ' replace this... '
    ACCESS_KEY = ' replace this... '
    ACCESS_SECRET = ' replace this... '
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)
    while(1):
        new_tweet = get_random_emoji_tweet()
        api.update_status(new_tweet)
        time.sleep(900) # Tweet every 15 minutes

if __name__ == "__main__":
    main()
