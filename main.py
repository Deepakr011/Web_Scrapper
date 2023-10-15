from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from flask import Flask
import threading
from datetime import datetime
from price import MyTask

# Create a Flask app for the HTTP server
app = Flask(__name__)

# Define a function to run the task
def send_message_job():
    my_task.get_HTML()

# Create an instance of the MyTask class
my_task = MyTask()

# Calculate the initial start time for today at 1:45 PM
now = datetime.now()
initial_start_time = now.replace(hour=15, minute=00, second=0, microsecond=0)

# Create a scheduler
scheduler = BackgroundScheduler()

# Define a cron trigger to run the job daily at the calculated initial start time
trigger = CronTrigger(
    year=initial_start_time.year,
    month=initial_start_time.month,
    day=initial_start_time.day,
    hour=initial_start_time.hour,
    minute=initial_start_time.minute,
)

# Add the job to the scheduler with a misfire grace time of 600 seconds
scheduler.add_job(send_message_job, trigger=trigger, misfire_grace_time=600)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=scheduler.start)
scheduler_thread.daemon = True
scheduler_thread.start()

@app.route('/')
def hello():
    return "Hello, this is your Flask server!"

# Run the Flask app on a specific port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    print("Flask server started successfully!")
