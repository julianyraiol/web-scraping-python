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

