import apscheduler.schedulers.background
from price import MyTask
from flask import Flask
import threading

# Create an instance of the MyTask class
my_task = MyTask()

# Create a scheduler
scheduler = apscheduler.schedulers.background.BackgroundScheduler({'apscheduler.job_defaults.max_instances': 2})


# Define a function to run the task
def send_message_job():
    my_task.get_HTML()

# Schedule the job to run every 2 minutes
scheduler.add_job(send_message_job, 'interval',seconds=600)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=scheduler.start)
scheduler_thread.daemon = True
scheduler_thread.start()

# Create a simple Flask app for the HTTP server
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, this is your Flask server!"

# Run the Flask app on a specific port
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
    print("Flask server started successfully!")
