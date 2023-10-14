# background_worker.py
from apscheduler.schedulers.blocking import BlockingScheduler
from price import MyTask

# Create an instance of the MyTask class
my_task = MyTask()

# Create a scheduler
scheduler = BlockingScheduler()

# Define a function to run the task
def send_message_job():
    my_task.get_HTML()

# Schedule the job to run every 2 minutes
scheduler.add_job(send_message_job, 'interval', minutes=2)

# Start the scheduler
scheduler.start()
