from scrapingcandidates import countSearch
import pyrebase

#Credencials#

config = {
  	"apiKey": "AIzaSyAsfXkYLuzqpCsrtM0zKxNqdQHCWuTSnsY",
	"authDomain": "recomenda-candidato.firebaseapp.com",
	"databaseURL": "https://recomenda-candidato.firebaseio.com",
	"projectId": "recomenda-candidato",
	"storageBucket": "recomenda-candidato.appspot.com",
	"messagingSenderId": "117502254794"
}

#Initialization#
firebase = pyrebase.initialize_app(config)

db = firebase.database()

#Functions
def createCandidate(name, group, url):
	data = {'name': name, 'group' : group}
	
	key = db.child('candidate').push(data)

	return key['name']

def scrapingCandidate(key, url):
	scraping = countSearch(url)

	data = {'link' : url, 'analysis' : scraping}
	db.child('candidate').child(key).child('url').push(data)	

#Call

name = 'Levi Fidelix'
group = 'PSC'
url = "http://congressoemfoco.uol.com.br/eleicoes-2014/programa-de-governo-de-levy-fidelix/"

key = createCandidate(name, group, url)
scrapingCandidate(key, url)
