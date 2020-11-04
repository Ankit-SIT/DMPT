# Ankit Das
# 19070122023
# Stable Marriage Problem in Python
# uses a list of dictionaries to store information

# change preferences only, rest are handled by the code


# /usr/bin/env python
# change names and preferences according to your need

males = [
    {
        "name": "A",
        "is_free": True,
        "gender": "male",
        "preferences": ["L", "J", "K", "M"],
        "engaged_to": "",
        "proposed_to":[],
    },
    {
        "name": "B",
        "is_free": True,
        "gender": "male",
        "preferences": ["J", "M", "L", "K"],
        "engaged_to": "",
        "proposed_to":[],
    },
    {
        "name": "C",
        "is_free": True,
        "gender": "male",
        "preferences": ["K", "M", "L", "J"],
        "engaged_to": "",
        "proposed_to":[],
    },
    {
        "name": "D",
        "is_free": True,
        "gender": "male",
        "preferences": ["M", "K", "J", "L"],
        "engaged_to": "",
        "proposed_to":[],
    }
]

females = [
    {
        "name": "J",
        "is_free": True,
        "gender": "female",
        "preferences": ["A", "D", "C", "B"],
        "engaged_to": "",
        "proposed_to":[],
    },
    {
        "name": "K",
        "is_free": True,
        "gender": "female",
        "preferences": ["A", "B", "C", "D"],
        "engaged_to": "",
        "proposed_to":[],
    },
    {
        "name": "L",
        "is_free": True,
        "gender": "female",
        "preferences": ["B", "D", "C", "A"],
        "engaged_to": "",
        "proposed_to":[],
    },
    {
        "name": "M",
        "is_free": True,
        "gender": "female",
        "preferences": ["C", "A", "B", "D"],
        "engaged_to": "",
        "proposed_to":[],
    }
]

def break_engagement(person):
    breakingWith = is_engaged_to(person)  # get the person engaged to 'person'

    for man in males: # check if person is in men first
        if man["name"] == person:
            if man["engaged_to"] != "": # make sure man is engaged before breaking
                man["engaged_to"] = ""  # set engaged woman to "" (null)
                man["is_free"] = True   # set is_free to True
                print("{} broke up with {}.".format(person, breakingWith))
                return True

    for woman in females:   # go to women if not found
        if woman["name"] == person:
            if woman["engaged_to"] != "": # make sure man is engaged before breaking
                woman["engaged_to"] = "" # set engaged woman to "" (null)
                woman["is_free"] = True # set is_free to True
                print("{} is breaking with {}.".format(person, breakingWith))
                return True


def is_engaged_to(person):  

    for man in males:   # check if person is in men first
        if man["name"] == person: # check if name of 'person' is the name of man
            return man["engaged_to"] #returns the woman engaged to 'person'

    for woman in females:   # go to women if not found
        if woman["name"] == person: # check if name of 'person' is the name of woman
            return woman["engaged_to"]  #returns the man engaged to 'person'

    return False


def is_engaged(person):
    for man in males:
        if man["name"] == person: # check for person in men
            if man["engaged_to"] != "":  # check if man is engaged i.e engaged_to = "NAME OF WOMAN"
                return True              # it meant that the man isn't engaged

    for woman in females:           # check for person in women
        if woman["name"] == person:
            if woman["engaged_to"] != "": # check if woman is engaged
                return True                 # if yes, return True

    return False                            # otherwise, return false


def choose_preference(person, candidate1, candidate2):
    for man in males:   # search for person in list of men
        if man["name"] == person:  # if found, 
            for i in range(0, len(males)):  # go through the list of males

                # return whichever candidate comes first
                if candidate1 == man["preferences"][i]: 
                    return candidate1
                if candidate2 == man["preferences"][i]:
                    return candidate2

    for woman in females: # search for person in list of women
        if woman["name"] == person: # if found
            for i in range(0, len(females)): # go through the list of females

                # return whichever candidate comes first
                if candidate1 == woman["preferences"][i]:
                    return candidate1
                if candidate2 == woman["preferences"][i]:
                    return candidate2


def engage(groom, bride):
    for man in males: # go through list of men
        if man["name"] == groom:   # find man with the name of the groom
            man["engaged_to"] = bride   # set engaged_to to bride
            man["is_free"] = False      # set engagement status to true

    for woman in females:  # go through  list of women
        if woman["name"] == bride:  # find woman with name of the bride
            woman["engaged_to"] = groom # set engaged_to to groom
            woman["is_free"] = False    # set engagement status to true


def get_name_from_ranking(groom, rank):
    for man in males:
        if man["name"] == groom:
            return man["preferences"][rank]


def menOptimal():
    while (True):
        numberOfPairs = len(males)
        good = 1
        for man in males:
            currentMan = man["name"]

            # if man has proposed to atleast one but not all
            if (man["is_free"] == False) and (len(man["proposed_to"]) != numberOfPairs):
                good += 1 
                if good == numberOfPairs: # if the men have gone through all phases of proposals,
                    print("\n\n\nSuccess!") # our work is done!
                    return

            for x in range(0, numberOfPairs):
                if not is_engaged(currentMan):
                    if x not in man["proposed_to"]:
                        man["proposed_to"].append(x)

                        woman = get_name_from_ranking(currentMan, x)

                        if is_engaged(woman): # if the woman is engaged
                            currentManOfTheEngaged = is_engaged_to(woman)  # get man engaged to woman

                            betterLover = choose_preference(               # choose which one is better
                                woman, currentManOfTheEngaged, currentMan)

                            engage(betterLover, woman)                     # engage whoever is better

                            if betterLover != currentManOfTheEngaged:      # if better person is not who the woman was engaged to earlier,
                                break_engagement(currentManOfTheEngaged)   # break engagement of the previous man
                        else:
                            engage(currentMan, woman)                        # if the woman hasn't been engaged yet, engage her to the current Man

def womenOptimal():
    while (True):
        numberOfPairs = len(females)
        good = 1
        for woman in females:
            currentWoman = woman["name"]

            # if woman has proposed to atleast one but not all
            if (woman["is_free"] == False) and (len(woman["proposed_to"]) != numberOfPairs):
                good += 1 
                if good == numberOfPairs: # if the women have gone through all phases of proposals,
                    print("\n\n\nSuccess!") # our work is done!
                    return

            for x in range(0, numberOfPairs):
                if not is_engaged(currentWoman): # if current woman isn't engaged
                    if x not in woman["proposed_to"]: # check if man is not in the list of previously engaged men
                        woman["proposed_to"].append(x)

                        man = get_name_from_ranking(currentWoman, x) # get name of man from ranking x

                        if is_engaged(man): # if the man is engaged
                            currentWomanOfTheEngaged = is_engaged_to(man)  # get man engaged to woman

                            betterLover = choose_preference(               # choose which one is better
                                man, currentWomanOfTheEngaged, currentWoman)

                            engage(man, betterLover)                     # engage whoever is better

                            if betterLover != currentWomanOfTheEngaged:      # if better person is not the previous man ,
                                break_engagement(currentWomanOfTheEngaged)   # break engagement of the previous woman
                        else:
                            engage(man, currentWoman)                        # if the man hasn't been engaged yet, engage him to the current woman


def main():   # driver function
    menOptimal()
    womenOptimal()
    showResult()


def showResult(): # function to print results
    print("Resolution:\n")
    for man in males:
        groom = man["name"] # get name of groom
        bride = man["engaged_to"] # get name of bride

        print("{} IS ENGAGED TO {}".format(groom, bride))
    
    print('\n')

    for woman in females:
        bride = woman["name"] # get name of groom
        groom = woman["engaged_to"] # get name of bride

        print("{} IS ENGAGED TO {}".format(bride, groom))


if __name__=="__main__":
    try:
        main()

    except KeyboardInterrupt:  # handle exit when CTRL+C is pressed
        print("EXITING PROGRAM!")
        exit(0)
    
