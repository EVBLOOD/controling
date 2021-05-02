import sched, time
from requests import Session
from bs4 import BeautifulSoup as bs
from testMail import Mail
import random

#to use sched
timer = sched.scheduler(time.time,time.sleep)
#the loging function
def bot(Timer) :
    #target link and loading page
    loglink = 'https://example.etc/'
    targetlink = 'https://example.etc/next'
    #start the session
    with Session() as s:
        #find and get the token
        while True: #to get the authenticity token if the login needs it
            site = s.get(loglink)
            content = bs(site.content, "html.parser")
            try :
                token = content.find("input", {"name":"authenticity_token"})["value"]
            except :
                token = ''
            if token != '':
                break
            else :
                print('just keep wait to connect...')
    #All what's nessaisaire to log
    payload = {
    'authenticity_token': token,
    'email': 'example@example.etc',
    'password': 'tirarara',
    'commit': 'Sign in'}
    #send a post request to the login page
    s.post(loglink,payload)
    #getting the target page content
    targetpage = s.get(targetlink)
    soup = bs(targetpage.content,'html.parser')
    content = soup.prettify()
    if ('<tr>' or '<td>' or '</td>') in content :
        #get notify via gmail if the condition is true and a tag has been added to the website
        mail = Mail("example@example.etc" , "tirarara") #gmail,password
        mail.send("example1@example.etc", "subject", "Text") #email recept,subject,text
        mail.send("example2@example.etc", "subject", "Text")
        mail.send("example3@example.etc", "subject", "Text")
        mail.send("example4@example.etc", "subject", "Text")
        mail.close()
    else :
        print('Keep waiting...')
    c = random.randint(0, 10)
    print('next start after',c,'s')
    timer.enter(c,1,bot,(Timer,)) #to loop
#to run
timer.enter(0,1,bot,(timer,))
timer.run()
