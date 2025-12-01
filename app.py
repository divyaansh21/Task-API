from flask import Flask
import logging as logger
logger.basicConfig(level="DEBUG")

flaskAppInstance=Flask(__name__)

@flaskAppInstance.route('/')
def home():
    return "<h1>Project Aether is Live!</h1>", 200

if(__name__=="__main__"):
	logger.debug("Starting the app")
	from api import *
	flaskAppInstance.run(host="0.0.0.0",port=5000,debug=False)
 
