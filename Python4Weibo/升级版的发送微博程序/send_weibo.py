#! /usr/bin/python

from initclient import initclient
#
# APP_KEY = 'your_key'
# APP_SECRET = 'your_secret'
# CALL_BACK = 'your_callback'

APP_KEY = '885594759'
APP_SECRET = '2e1e21ee3d40d8267dc675de31fbf5e4'
# CALL_BACK = 'http://bingbingrobot.sinaapp.com/'
CALL_BACK = 'https://api.weibo.com/oauth2/default.html'

def run():
    client = initclient.get_client(APP_KEY, APP_SECRET, CALL_BACK)

    while True:
        print "Ready! Do you want to send a new weibo?(y/n)"
        choice = raw_input()
        if choice == 'y' or choice == 'Y':
            content = raw_input('input the your new weibo content : ')
            if content:
                client.statuses.update.post(status=content)
                print "Send succesfully!"
                break
            else:
                print "Error! Empty content!"
        if choice == 'n' or choice == 'N':
            break

if __name__ == "__main__":
    run()
