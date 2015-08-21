__author__ = 'Jin'
# -*- coding: utf-8 -*-
from flask import Flask, jsonify
import requests

app = Flask(__name__)
app.config["DEBUG"] = True


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
