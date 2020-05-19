from flask import Flask
from flask import render_template
from flask_apscheduler import APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
 
import time
 
app = Flask(__name__)

#TODO: add the code for the ApScheduler here


 
@app.route('/')
def welcome():
 scheduler = BackgroundScheduler({'apscheduler.timezone':'America/Los_Angeles'})
 scheduler.add_job(job,'interval', hours=3)
 scheduler.start()
 return render_template('home.html')
def job:
 return print('Hey, get back to work!')
  
if __name__=="__main__":
    app.run(debug=False)
