from apscheduler.schedulers.background import BackgroundScheduler
from price import MyTask
from flask import Flask
import threading

# Create an instance of the MyTask class
my_task = MyTask()

# Create a scheduler
scheduler = BackgroundScheduler(max_instances=1)  # Set max_instances to 1

# Define a function to run the task
def send_message_job():
    my_task.get_HTML()

# Schedule the job to run every 20 seconds
scheduler.add_job(send_message_job, 'interval', seconds=20)

# Start the scheduler in a separate thread
scheduler_thread = threading.Thread(target=scheduler.start)
scheduler_thread.daemon = True
scheduler_thread.start()

# Create a simple Flask app for the HTTP server
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello, this is your Flask server!"

if __name__ == '__main__':
    # Start the Flask app after the scheduler is initialized
    app.run(host='0.0.0.0', port=5000)
    print("Flask server started successfully!")
