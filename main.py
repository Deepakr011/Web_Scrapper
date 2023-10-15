from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask import Flask
from price import MyTask
import threading

# Create a Flask app for the HTTP server
app = Flask(__name__)

# Define a function to run the task
def send_message_job():
    my_task.get_HTML()

# Create an instance of the MyTask class
my_task = MyTask()

# Create a scheduler
scheduler = BackgroundScheduler()

trigger = CronTrigger(second=0, minute=0, hour=9)
scheduler.add_job(send_message_job, trigger=trigger, misfire_grace_time=600)


scheduler_thread = threading.Thread(target=scheduler.start)
scheduler_thread.daemon = True
scheduler_thread.start()

@app.route('/')
def hello():
    return "Hello, this is your Flask server!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    print("Flask server started successfully!")
