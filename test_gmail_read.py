#==============================================================================================================
# (c) 2020 real-4w, based on https://www.thepythoncode.com/article/reading-emails-in-python
#==============================================================================================================
# Make sure you have a file called "kl.yaml" in the CWD, containing variables as follows:
#debug : True
#username : <your email>@gmail.com
#password : <yourpassword | yourapplicationpassword>
#==============================================================================================================
import imaplib, email, yaml, sys
from email.header import decode_header
import webbrowser, os

def ProcessYAML (yaml_file) :
    '''This function opens the yaml file and returns the data object'''
    with open(yaml_file) as f:
        y_data = yaml.load(f, Loader=yaml.FullLoader)
        debug = y_data['debug']
        if debug == True : print("YAML file:\n", y_data)
    return (y_data, debug) 
def parse_mailbox(data):
    flags, b, c = data.partition(' ')                                         # searches and splits the string into a tuple containing three elements before, string, after
    separator, b, name = c.partition(' ')
    return (flags, separator.replace('"', ''), name.replace('"', ''))         
yaml_data, debug = ProcessYAML('kl.yaml')                                   # yaml settings are global variables
username = yaml_data['username']                                            # account credentials
password = yaml_data['password']
if debug == True :
    print("Email", username, password)

no_mes = 3                                                                  # number of top emails to fetch
imap = imaplib.IMAP4_SSL("imap.gmail.com")                                  # create an IMAP4 class with SSL, use your email provider's IMAP server
imap.login(username, password)                                              # authenticate

if debug == True :
    #res, label = imap.list("[Gmail]")
    res, label = imap.list()                                                # use imap.list() to get the list of mailboxes
    if res == 'OK':
        for mbox in label :
            flags, separator, name = parse_mailbox(bytes.decode(mbox))      # decode a stream of bytes to a string object,
            print(name)
        input("Press any key to continue.")
status, messages = imap.select("INBOX")                                     # select a mailbox (in this case, the inbox mailbox)
messages = int(messages[0])                                                 # total number of emails
if debug == True :
    print(f"Number of messages: {messages}")
    print(messages)
for i in range(messages, messages - no_mes, -1):
    if debug == True : print(i)
    res, msg = imap.fetch(str(i), "(RFC822)")                               # fetch the email message by ID
    for response in msg:
        if isinstance(response, tuple):
            # parse a bytes email into a message object
            msg = email.message_from_bytes(response[1])
            # decode the email subject
            subject = decode_header(msg["Subject"])[0][0]
            if isinstance(subject, bytes):
                # if it's a bytes, decode to str
                subject = subject.decode()
            # email sender
            from_ = msg.get("From")
            print("From:", from_)
            print("Subject:", subject)
                        # if the email message is multipart
            #if msg.is_multipart():
            #    # iterate over email parts
            #    for part in msg.walk():
            #        # extract content type of email
            #        content_type = part.get_content_type()
            #        content_disposition = str(part.get("Content-Disposition"))
            #        try:
            #            # get the email body
            #            body = part.get_payload(decode=True).decode()
            #        except:
            #            pass
            #        if content_type == "text/plain" and "attachment" not in content_disposition:
            #            # print text/plain emails and skip attachments
            #            print(body)
            #        elif "attachment" in content_disposition:
            #            # download attachment
            #            filename = part.get_filename()
            #            if filename:
            #                if not os.path.isdir(subject):
            #                    # make a folder for this email (named after the subject)
            #                    os.mkdir(subject)
            #                filepath = os.path.join(subject, filename)
            #                # download attachment and save it
            #                open(filepath, "wb").write(part.get_payload(decode=True))
            #else:
            #    # extract content type of email
            #    content_type = msg.get_content_type()
            #    # get the email body
            #    body = msg.get_payload(decode=True).decode()
            #    if content_type == "text/plain":
            #        # print only text email parts
            #        print(body)
            #if content_type == "text/html":
            #    print("HTML")
                # if it's HTML, create a new HTML file and open it in browser
                #if not os.path.isdir(subject):
                #    # make a folder for this email (named after the subject)
                #    os.mkdir(subject)
                #filename = f"{subject[:50]}.html"
                #filepath = os.path.join(subject, filename)
                # write the file
                #open(filepath, "w").write(body)
                # open in the default browser
                #webbrowser.open(filepath)

            print("="*100)

# close the connection and logout
imap.close()
imap.logout()