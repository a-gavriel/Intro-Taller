import csv, json, random

## global variable of score for easy access
global scores
scores = []


def getindexscore( user_data):
    global scores
    if int(user_data[1]) > int(scores[1][1]):
        return 1
    elif int(user_data[1]) > int(scores[2][1]):
        return 2
    elif int(user_data[1]) > int(scores[3][1]):
        return 3
    elif int(user_data[1]) > int(scores[4][1]):
        return 4
    elif int(user_data[1]) > int(scores[5][1]):
        return 5
    else:
        return -1

def replacescore( user_data, index):
    global scores
    if index == 5:
        scores[5] = user_data
    elif index == 4:
        scores [5] = scores[4]
        scores[4] = user_data
    elif index == 3:
        scores[5] = scores[4]
        scores[4] = scores[3]
        scores[3] = user_data
    elif index == 2:
        scores[5] = scores[4]
        scores[4] = scores[3]
        scores[3] = scores[2]
        scores[2] = user_data
    elif index == 1:
        scores[5] = scores[4]
        scores[4] = scores[3]
        scores[3] = scores[2]
        scores[2] = scores[1]
        scores[1] = user_data

def readcsv():
    global scores
    scores = []
    with open('scores.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            scores += [row]
    
    csvFile.close()

def main():
    global scores

    #la tabla
    scores = [["Nombre","Score"]]+[["None","100"]]*5
    print (scores)

    loadCSV = False

    if loadCSV:
        readcsv()
        print("changed scores from file:")
        print(scores)

    ## current user score and name
    user_name = 'A' + str(random.randint(1, 100))
    user_score = random.randint(1, 1000)
    
    


    ## places the player data in the top5 scoreboard

    user_data = [user_name, str(user_score)]
    print(user_data)
    scoreboardindex = getindexscore(user_data)
    if (scoreboardindex != -1):
        replacescore(user_data, scoreboardindex)

    print(scores)


    ## generates CSV

    with open('scores.csv','r+') as outfilecsv:
        writer = csv.writer(outfilecsv)
        writer.writerows(scores)
    outfilecsv.close()


    ## generates JSON from CSV
    jsonfile = open("scores.json", "w+")
    with open("scores.csv","r+") as csvfile:
        next(csvfile,None)
        reader = csv.DictReader(csvfile,fieldnames = ["Name","Score"])
        json.dump([row for row in reader],jsonfile)
    
    jsonfile.close()
    csvfile.close()

main()
