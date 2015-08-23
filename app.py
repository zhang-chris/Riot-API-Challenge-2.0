__author__ = 'Jin'
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import requests


app = Flask(__name__)
app.config["DEBUG"] = False





def getMatchIDs(region):
	
	directory = "AP_ITEM_DATASET/5.11/NORMAL_5X5/" + region + ".json"
	infile = open(directory, "r")
	matchList = infile.read()
	matchList = matchList.lstrip("[\n").rstrip("]\n").replace("\n", "").split(", ")


	
	infile.close()
	return matchList

def writeStats(matchList, region):

	directory = "MATCH_NA_DATA/" + region + "data.json"
	outfile = open(directory, "w")
	for i in range(0, 1):
		matchID = matchList[i]
		url = "https://na.api.pvp.net/api/lol/na/v2.2/match/" + matchID + "?api_key=0f9be0c6-c095-4010-8036-e9ce291f8117"
		response_dict = requests.get(url).json()
		for j in range(0, 10):
			
			matchData = []
			matchData.append(matchID)
			participants = response_dict['participants'][j]

			stats = participants['stats']

			championID = participants['championId']
			print (championID)
			url2 = "https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion/" + str(championID) + "?champData=tags&api_key=0f9be0c6-c095-4010-8036-e9ce291f8117"
			response_dict2 = requests.get(url2).json()
			print (response_dict2)
			champion = response_dict2['tags']


			matchData.append(participants['timeline']['role'])
			matchData.append(participants['timeline']['lane'])
			
			#3-11
			matchData.append(stats['totalDamageDealt'])
			matchData.append(stats['totalDamageTaken'])	
			matchData.append(stats['magicDamageDealt'])			
			matchData.append(stats['magicDamageTaken'])
			matchData.append(stats['physicalDamageDealt'])
			matchData.append(stats['physicalDamageTaken'])
			matchData.append(stats['magicDamageDealtToChampions'])
			matchData.append(stats['physicalDamageDealtToChampions'])
			matchData.append(stats['totalDamageDealtToChampions'])

			#12-17
			matchData.append(stats['item1'])
			matchData.append(stats['item2'])
			matchData.append(stats['item3'])
			matchData.append(stats['item4'])
			matchData.append(stats['item5'])
			matchData.append(stats['item6'])

			matchData.append(response_dict2['name'])
			for i in champion:
				matchData.append(i)
			if len(champion) == 1:
				matchData.append("None")
			
			matchDataString = str(matchData) + '\n'
			
			outfile.write(matchDataString)



	outfile.close()

def statsCounter():

	infile = open("MATCH_NA_DATA/NAdata.json", 'r')
	outfile = open("ITEM_DATA/NA.json", 'w')
	
	itemDict = {}

	for line in infile:
		lineList = line.lstrip("[").rstrip("]\n").split(", ")
		print (lineList)
		for i in range(12, 18):
			if lineList[i] in itemDict:
				itemDict[lineList[i]] += 1
			else:
				itemDict[lineList[i]] = 1
		for i in range(3, 12):
			if i in itemDict:
				itemDict[i] += int(lineList[i])
			else:
				itemDict[i] = int(lineList[i])
	outfile.write(str(itemDict))
	infile.close()
	outfile.close()







@app.route("/")
def hello():
	return "League of Legends"

@app.route("/search/<search_query>")
def search(search_query):
	url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/LOLSAURUS/" + search_query + "?api_key=0f9be0c6-c095-4010-8036-e9ce291f8117"
	response_dict = requests.get(url).json()
	return jsonify(response_dict)

@app.route("/test")
def test():
	url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/LOLSAURUS?api_key=0f9be0c6-c095-4010-8036-e9ce291f8117"
	response_dict = requests.get(url).json()
	print (response_dict)
	
	print (summonerid)

	# return jsonify(response_dict)

	return "testing"

# @app.route("/name")
# def summoner():
# 	url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/ "?api_key=0f9be0c6-c095-4010-8036-e9ce291f8117"
# 	response_dict = requests.get(url).json()
# 	return jsonify(response_dict)	

@app.route("/<name>/<query>")
def getID(name, query):
	url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + name + "?api_key=0f9be0c6-c095-4010-8036-e9ce291f8117"
	response_dict = requests.get(url).json()
	summonerid = str(response_dict[name]["id"])
	url = "https://na.api.pvp.net/api/lol/na/v1.4/summoner/" + summonerid + "/" + query + "?api_key=0f9be0c6-c095-4010-8036-e9ce291f8117"
	response_dict = requests.get(url).json()
	return jsonify(response_dict)
	# return response_dict[query]["id"]



testmatchid = getMatchIDs("NA")
writeStats(testmatchid, "NA")
statsCounter()


if __name__ == "__main__":
    app.run(host="0.0.0.0")

# app = Flask(__name__)
# app.config["DEBUG"] = True  # Only include this while you are testing your app

# everyWord = []
# sdict = {}
# finalAverage = .134793800734
# allVariance = []
# allStepOneZScore = []
# allZScore = []
# stdDev = .0117502795871

# def getfromurl(task):
#     url = "http://api.culpa.info"
#     url += task
#     response = requests.get(url)
#     return response.json()

# def reviews(response_dict):
#     if response_dict["status"] == "success":
#         review_text = []
#         for i in response_dict["reviews"]:
#             if "review_text" in i:
#                 review_text.append(i["review_text"].encode(encoding='UTF-8', errors='strict'))
#         return review_text
#     else:
#         return []

# def tolist(review_text):
#     for i in review_text:
#         eachSentenceEachReview = i.split(".")
#         everySentence = []
#         for j in eachSentenceEachReview:
#             eachWordEachSentence = j.split(" ")
#             everySentence.append(eachWordEachSentence)
#         everyWord.append(everySentence)


# def sentiment():
#     with open("sentiments.csv", 'r') as csvfile:
#         sfile = csv.reader(csvfile)
#         for row in sfile:
#             sdict[row[0]] = float(row[1])

# def averageEntireReview():
#     totalSentiment = 0
#     words = 0
#     for i in everyWord:
#         for j in i:
#             for k in j:
#                 if k in sdict:
#                     totalSentiment += sdict[k]
#                     words+=1
#     if words > 0:
#         return totalSentiment/words
#     else:
#         return 0

# def averageAllReviews():
#     totalAverage = 0
#     reviewscounted = 0
#     totalcounted = 0
#     for i in range(5000):
#         tolist(reviews(getfromurl("/reviews/review_id/" + str(i))))
#         averageThisReview = averageEntireReview()
#         totalAverage+=averageThisReview
#         totalcounted+=1
#         if averageThisReview != 0:
#             reviewscounted+=1
#         print(reviewscounted)
#     finalAverage = totalAverage/reviewscounted
#     print(finalAverage)


# def doStats():
#     reviewscounted = 0
#     for i in range(2000):
#         tolist(reviews(getfromurl("/reviews/review_id/" + str(i))))
#         averageThisReview = averageEntireReview()
#         if averageThisReview != 0:
#             reviewscounted += 1
#         print(storeVariance(averageThisReview), reviewscounted)
#     findstdDev(reviewscounted)


# def storeVariance(averageThisReview):
#     if averageThisReview != 0:
#         allVariance.append((averageThisReview - finalAverage) * (averageThisReview - finalAverage))
#         return (averageThisReview - finalAverage) * (averageThisReview - finalAverage)
#     else:
#         allVariance.append(0)
#         return 0

# def findstdDev(reviewscounted):
#     global stdDev
#     totalVariance = 0
#     for i in allVariance:
#         totalVariance += i
#     stdDev = math.sqrt(totalVariance/(reviewscounted - 1))
#     print(stdDev)

# def findZScore(reviewScore):
#     return (reviewScore - finalAverage)/stdDev

# def storeStepOneZScore(averageThisReview):
#     if averageThisReview != 0:
#         ZScore = (averageThisReview - finalAverage)
#         allStepOneZScore.append(ZScore)
#     else:
#         allStepOneZScore.append(0)

# def storeStepTwoZScore(standarddeviation):
#     for i in allStepOneZScore:
#         if i != 0:
#             allZScore.append(i / standarddeviation)
#         else:
#             allZScore.append(0)

# sentiment()

# def normalize(id):
#     tolist(reviews(getfromurl("/reviews/professor_id/" + str(id))))
#     professorZScore = findZScore(averageEntireReview())
#     return str(professorZScore)

# def summary(id):
#     review_text = reviews(getfromurl("/reviews/professor_id/" + str(id)))
#     tolist(review_text)
#     averageForProfessor = averageEntireReview()
#     sentimentEachReview = []
#     for i in review_text:
#         totalSentiment = 0
#         words = 0
#         eachWordEachReview = i.split(" ")
#         for j in eachWordEachReview:
#             if j in sdict:
#                 totalSentiment += sdict[j]
#                 words += 1
#         if words > 0:
#             sentimentEachReview.append(totalSentiment / words)
#         else:
#             sentimentEachReview.append(0)
#     tempClosestIndex = 0
#     current = 0
#     for i in sentimentEachReview:
#         if abs(i - averageForProfessor) < abs(sentimentEachReview[tempClosestIndex] - averageForProfessor):
#             tempClosestIndex = current
#         current+=1
#     return review_text[tempClosestIndex]

# @app.route("/")
# def home():
#     return render_template("home.html")

# @app.route("/search", methods=["GET", "POST"])
# def search():
#     if request.method == "POST":
#         url = "http://api.culpa.info/professors/search/" + request.form["user_search"]
#         response_dict = requests.get(url).json()
#         print(response_dict["professors"][0]["id"])
#         return render_template("results.html", api_data = response_dict)

#     else:
#         return render_template("search.html")

#     return render_template("search.html")

# @app.route("/<id>")
# def professorSummary(id):
#     professorZScore = str(round(float(normalize(id)), 3))
#     professorsummary = summary(id)
#     return render_template("sentiment.html", score = professorZScore, summary = professorsummary)

# if __name__ == '__main__':
#     app.run()
