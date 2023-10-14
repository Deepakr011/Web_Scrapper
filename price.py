from selenium import webdriver
from bs4 import BeautifulSoup
from twilio.rest import Client
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class MyTask:
    def __init__(self):
        self.html_list = []

    def error_send(self,error):
        sender_email = 'deepakr948267@gmail.com'
        sender_password = 'fnln nzvs beec frno'
        recipient_email = 'deepakr948267@gmail.com'
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = 'Areca_price_send_project'
        message = f'Massage is not send:\n{error}'
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
    def get_HTML(self):
        try:
            chromedriver_path = r"E:\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe"
            options = webdriver.ChromeOptions()
            options.add_argument('--headless')
            driver = webdriver.Chrome(executable_path=chromedriver_path, options=options)
            url = 'https://www.krishimaratavahini.kar.nic.in/MainPage/DailyMrktPriceRep2.aspx?Rep=Com&CommCode=140&VarCode=1&Date=12/10/2018&CommName=Arecanut%20/%20%E0%B2%85%E0%B2%A1%E0%B2%BF%E0%B2%95%E0%B3%86&VarName=Red%20/%20%E0%B2%95%E0%B3%86%E0%B2%82%E0%B2%AA%E0%B3%81'
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')

            table = soup.find('table', id='_ctl0_content5_Table1')

            rows = table.find_all('tr')
            self.get_data(rows)
        except Exception as error:
            print(error)
            self.error_send(error)



    def get_data(self, rows):
        try:
            for row in rows:
                if 'SHIVAMOGGA' in row.get_text() and 'Rashi' in row.get_text():
                    self.html_list.append(row)
                if 'SAGAR' in row.get_text() and 'Rashi' in row.get_text():
                    self.html_list.append(row)

            for i in range(len(self.html_list)):
                self.html_list[i] = self.html_list[i].prettify()
                self.html_list[i] = BeautifulSoup(self.html_list[i], 'html.parser')
            sagar = self.html_list[0].findAll("td")
            shimoga = self.html_list[1].findAll("td")
            message = (
                f'SAGAR:{sagar[1].get_text().strip()}\nRS:{sagar[5].get_text().strip()}\nSHIVAMOGGA:{shimoga[1].get_text().strip()}\nRS:{shimoga[5].get_text().strip()}')
            self.send_message(message)
        except Exception as error:
            print(error)
            self.error_send(error)


    def send_message(self, message):
        try:
            SID = 'AC82489ab4391dd62ef168df8fc3e2159d'
            AUTH_TOKEN = '37abf777c3e93ae6446aee51834d99c3'

            cl = Client(SID, AUTH_TOKEN)

            cl.messages.create(body=f"{message}", from_='+12293983881', to='+91 93808 87409')
        except Exception as error:
            print(error)
            self.error_send(error)




