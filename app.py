from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for, send_from_directory
app = Flask(__name__)

import mysql.connector
from mysql.connector import errorcode


# Obtain connection string information from the portal
# production:
config = {
  'host':'python-mysql-sample-server.mysql.database.azure.com',
  'user':'gsoedfdakr',
  'password':'U0B2155QI15WSUS0$',
  'database':'python-mysql-sample-database'
}

# test (local):
# config = {
#   'host':'localhost',
#   'user':'robert.tracey',
#   'password':'i.r8D8UgyeltJ_wC',
#   'database':'python_sample'
# }

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')   

   if name:     
       # add_name(name)  
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))


if __name__ == '__main__':
   app.run()