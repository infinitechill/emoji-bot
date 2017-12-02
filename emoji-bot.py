#! /usr/local/bin/python3
# infinite chill / 2017

import sys, time, random, emoji, tweepy


leafs = {
"Maple Leaf" : "🍁", 
"Fallen Leaf" : "🍂", 
"Leaf Fluttering in Wind" : "🍃"
}

flyingbugs = {
"Honeybee" : "🐝",
"Butterfly" : "🦋"
}

gardenbugs = {
"Snail" : "🐌", 
"Bug" : "🐛", 
"Ant" : "🐜", 
"Lady Beetle" : "🐞" 
}

plants = {
"plant1" : ":seedling:", 
"plant2" : ":hibiscus:", 
"plant3" : ":blossom:", 
"plant4" : ":cherry_blossom:", 
"plant5" : ":mushroom:", 
"plant6" : ":sunflower:"
}

snow = {
"snow1" : "❄️",
"snow2" : "🌨"
}

snowmen = {
"snowmen1" : "☃️", 
"snowmen2" : "⛄️"
}

rain = {
"rain1" : "🌧", 
"rain2" : "💦", 
"rain3" : "⚡", 
"Droplet" : "💧"
}

umbrellas = {
"rain1" : "☂", 
"rain2" : "☔"
}

fish = {
"fish1" : "🐙", 
"fish2" : "🐠",
"fish3" : "🐟",
"fish5" : "🐡",
"fish5" : "🐠"
}

aquaplants = {
"aquaplant1" : "🌱",
"aquaplant2" : "🌿",
"aquaplant3" : "🌾"
}

airscene = {
"airscene1" : "🕊️",
"airscene2" : "✈️",
"airscene3" : "🛩️",
"airscene4" : "🚁",
"airscene5" : "☁️"
} 

forestplants = {
"Evergreen Tree" : "🌲", 
"Deciduous Tree" : "🌳", 
"Palm Tree" : "🌴"
} 

forestanimals = {
"Gorilla" : "🦍", 
"Mouse" : "🐁", 
"Rat" : "🐀", 
"Rabbit" : "🐇", 
"Chipmunk" : "🐿",
"Eagle" : "🦅",
"Owl" : "🦉",
"Owl" : "🐢",
} 

flowergarden =  {
"Bouquet" : "💐", 
"Cherry Blossom" : "🌸", 
"White Flower" : "💮", 
"Rosette" : "🏵", 
"Rose" : "🌹",  
"Hibiscus" : "🌺", 
"Sunflower" : "🌻", 
"Blossom" : "🌼", 
"Tulip" : "🌷",
"Seedling" : "🌱",
"Herb" : "🌿",
"Blossom" : "🌼",
"Shamrock" : "☘", 
"Four Leaf Clover" : "🍀",
}

otherplants = {
"Cactus" : "🌵", 
"Sheaf of Rice" : "🌾",
"Mushroom" : "🍄", 
"Chestnut" : "🌰"
}



death = {
"Scorpion" : "🦂", 
"Spider" : "🕷️",
"Skull" : "💀", 
"Spider Web" : "🕸️",
"Flame" : "🔥", 
"Cigarette" : "🚬",
"Pill" : "💊", 
"Syringe" : "💉",
"Sword" : "🗡", 
"Skull and Crossbones" : "☠️",
"Devil" : "😈", 
"Ogre" : "👹",
"Sign of the Horns" : "🤘", 
"Pirate Flag" : "🏴‍☠️",
"Bomb" : "💣", 
"Black Flag" : "🏴",
"Kitchen Knife" : "🔪", 
"Crossed Swords" : "⚔",
"Ghost" : "👻"
}


def get_random_garden():
    myleafs = list(leafs.values())
    mybugs = list(gardenbugs.values())
    myflying = list(flyingbugs.values())
    myplants = list(otherplants.values())
    result_string=""
    # vertical length
    last_used=""
    for i in range(5):
        count=0
        # width of scene
        for i in range(35):
            # 1/20 chance
            todo=random.randint(0,20)
            if todo == 0:
                # 1/5 chance
                todo=random.randint(0,5)
                if todo == 0:
                    randomindex=random.randint(0, len(myflying)-1 )
                    result_string += emoji.emojize(myflying[randomindex], use_aliases=True) + " "
                    last_used=myflying[randomindex]
                else:
                    randomindex=random.randint(0, len(myleafs)-1 )    
                    while( myleafs[randomindex] == last_used):
                        randomindex=random.randint(0, len(myleafs)-1 )
                    result_string += emoji.emojize(myleafs[randomindex], use_aliases=True) + " "
                    last_used=myleafs[randomindex]
                count+=1               
            # no emoji, print a space...
            else:
                result_string += " "
            # if we have reached max emojis, pass
            if count == 2:
                break
        result_string += "\n"

    count=0
    for i in range(35):
        todo=random.randint(0,5)
        if todo == 0:
            randomindex=random.randint(0, len(mybugs)-1 )
            while( mybugs[randomindex] == last_used ):
                randomindex=random.randint(0, len(mybugs)-1 )
            result_string += emoji.emojize(mybugs[randomindex], use_aliases=True) + " "
            last_used=mybugs[randomindex]
            count+=1
        elif todo == 1:
            randomindex=random.randint(0, len(myplants)-1 )
            while( myplants[randomindex] == last_used ):
                randomindex=random.randint(0, len(myplants)-1 )
            result_string += emoji.emojize(myplants[randomindex], use_aliases=True) + " "
            last_used=myplants[randomindex]
            count+=1            

        else:
            result_string += " "
        if count == 3:
            break
    return result_string



def get_random_snow():
    mysnow = list(snow.values())
    mysnowmen = list(snowmen.values())
    result_string=""
    # sky
    last_used=""
    for i in range(5):
        count=0
        # width of scene
        for i in range(35):
            # 1/20 chance
            todo=random.randint(0,20)
            if todo == 0:
                # 1/5 chance
                todo=random.randint(0,5)
                if todo == 0:
                    randomindex=random.randint(0, len(mysnow)-1 )
                    result_string += emoji.emojize(mysnow[randomindex], use_aliases=True) + " "
                    last_used=mysnow[randomindex]
                else:
                    randomindex=random.randint(0, len(mysnow)-1 )    
                    while( mysnow[randomindex] == last_used):
                        randomindex=random.randint(0, len(snow)-1 )
                    result_string += emoji.emojize(mysnow[randomindex], use_aliases=True) + " "
                    last_used=mysnow[randomindex]
                count+=1               
            # no emoji, print a space...
            else:
                result_string += " "
            # if we have reached max emojis, pass
            if count == 3:
                break
        result_string += "\n"
    #ground
    count=0
    for i in range(35):
        todo=random.randint(0,5)
        if todo == 0:
            randomindex=random.randint(0, len(mysnowmen)-1 )
            while( mysnowmen[randomindex] == last_used ):
                randomindex=random.randint(0, len(mysnowmen)-1 )
            result_string += emoji.emojize(mysnowmen[randomindex], use_aliases=True) + " "
            last_used=mysnowmen[randomindex]
            count+=1
        else:
            result_string += " "
        if count == 3:
            break
    return result_string



def get_random_rain():
    myrain = list(rain.values())
    myumbrellas = list(umbrellas.values())
    result_string=""
    last_used=""
    # sky
    for i in range(5):
        count=0
        # width of scene
        for i in range(35):
            # 1/10 chance
            todo=random.randint(0,10)
            if todo == 0:
                # 1/5 chance
                todo=random.randint(0,5)
                randomindex=random.randint(0, len(myrain)-1 )
                result_string += emoji.emojize(myrain[randomindex], use_aliases=True) + " "
                count+=1             
            # no emoji, print a space...
            else:
                result_string += " "
            # if we have reached max emojis, pass
            if count == 3:
                break
        result_string += "\n"
    #ground
    count=0
    for i in range(35):
        todo=random.randint(0,5)
        if todo == 0:
            randomindex=random.randint(0, len(myumbrellas)-1 )
            while( myumbrellas[randomindex] == last_used ):
                randomindex=random.randint(0, len(myumbrellas)-1 )
            result_string += emoji.emojize(myumbrellas[randomindex], use_aliases=True) + " "
            last_used=myumbrellas[randomindex]
            count+=1
        else:
            result_string += " "
        if count == 3:
            break
    return result_string


def get_random_flight():
    myflight = list(airscene.values())
    result_string=""
    # sky
    for i in range(5):
        # width of scene
        count=0
        for i in range(35):
            # 1/20 chance
            todo=random.randint(0,15)
            if todo == 0:
                randomindex=random.randint(0, len(myflight)-1 )    
                result_string += emoji.emojize(myflight[randomindex], use_aliases=True) + " "
                count+=1               
            elif todo == 1:
                result_string += emoji.emojize("☁️ ")
            # no emoji, print a space...
            else:
                result_string += " "
            # if we have reached max emojis, pass
            if count == 1:
                break
        result_string += "\n"
    return result_string


def get_random_forest():
    myforest = list(forestplants.values())
    myanimals = list(forestanimals.values())
    result_string=""
    # sky
    for i in range(5):
        # width of scene
        count=0
        for i in range(35):
            # 1/3 chance
            todo=random.randint(0,3)
            if todo == 0:
                # 1/20 chance
                todo=random.randint(0,20)
                if todo == 0:
                    randomindex=random.randint(0, len(myanimals)-1 )
                    result_string += myanimals[randomindex] + " "
                else:
                    randomindex=random.randint(0, len(myforest)-1 )    
                    result_string += myforest[randomindex] + " "
                count+=1               
            # no emoji, print a space...
            else:
                result_string += " "
            # if we have reached max emojis, pass
            if count == 5:
                break
        result_string += "\n"
    return result_string





def get_random_fish():
    myfish = list(fish.values())
    myplants = list(aquaplants.values())
    result_string=""
    # sky
    last_used=""
    for i in range(5):
        count=0
        # width of scene
        for i in range(35):
            # 1/20 chance
            todo=random.randint(0,20)
            if todo == 0:
                # 1/5 chance
                todo=random.randint(0,5)
                if todo == 0:
                    randomindex=random.randint(0, len(myfish)-1 )
                    result_string += emoji.emojize(myfish[randomindex], use_aliases=True) + " "
                    last_used=myfish[randomindex]
                else:
                    randomindex=random.randint(0, len(myfish)-1 )    
                    while( myfish[randomindex] == last_used):
                        randomindex=random.randint(0, len(snow)-1 )
                    result_string += emoji.emojize(myfish[randomindex], use_aliases=True) + " "
                    last_used=myfish[randomindex]
                count+=1               
            # no emoji, print a space...
            else:
                result_string += " "
            # if we have reached max emojis, pass
            if count == 2:
                break
        result_string += "\n"

    #ground
    count=0
    for i in range(35):
        todo=random.randint(0,5)
        if todo == 0:
            randomindex=random.randint(0, len(myplants)-1 )
            while( myplants[randomindex] == last_used ):
                randomindex=random.randint(0, len(myplants)-1 )
            result_string += emoji.emojize(myplants[randomindex], use_aliases=True) + " "
            last_used=myplants[randomindex]
            count+=1
        else:
            result_string += " "
        if count == 3:
            break
    return result_string



def get_random_flower_garden():
    myflowers = list(flowergarden.values())
    result_string=""
    # sky
    for i in range(5):
        # width of scene
        for i in range(35):
            todo=random.randint(0,5)
            if todo == 0:
                randomindex=random.randint(0, len(myflowers)-1 )    
                result_string += myflowers[randomindex] + " "              
            # no emoji, print a space...
            else:
                result_string += " "
        result_string += "\n"
    return result_string


def get_random_death():
    mydeath = list(death.values())
    result_string=""
    # sky
    for i in range(5):
        # width of scene
        for i in range(35):
            todo=random.randint(0,10)
            if todo == 0:
                randomindex=random.randint(0, len(mydeath)-1 )    
                result_string += mydeath[randomindex] + " "              
            # no emoji, print a space...
            else:
                result_string += " "
        result_string += "\n"
    return result_string




def main():    
    CONSUMER_KEY = 'please fill in this with the information provided by twitter'
    CONSUMER_SECRET = 'please fill in this with the information provided by twitter'
    ACCESS_KEY = 'please fill in this with the information provided by twitter'
    ACCESS_SECRET = 'please fill in this with the information provided by twitter'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)


    while(1):
        todo=random.randint(0,7)
        if (todo == 0):
            new_tweet = get_random_garden()
        elif (todo == 1):
            new_tweet = get_random_snow()
        elif (todo == 2):  
            new_tweet = get_random_rain()
        elif (todo == 3):  
            new_tweet = get_random_flight()
        elif (todo == 4):  
            new_tweet = get_random_forest()
        elif (todo == 5): 
            new_tweet = get_random_flower_garden()
        elif todo == 6:
            new_tweet = get_random_fish()
        else:
            new_tweet = get_random_death()

        #print()
        #print(new_tweet)
        #print()
        api.update_status(new_tweet)
        # Tweet every 15 minutes
        time.sleep(900) 

if __name__ == "__main__":
    main()
