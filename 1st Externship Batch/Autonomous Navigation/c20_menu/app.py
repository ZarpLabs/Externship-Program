#!/usr/bin/env python
from flask import *  

value = 0

app = Flask(__name__)  
      
@app.route('/login',methods = ['POST'])  
def login():  
  uname=request.form['number']  
  #passwrd=request.form['pass']  
  if uname=="A": 
  #   global value
  #   value = 1
  #   print(value)
    lines = ["1"]
    with open('readme.txt', 'w') as f:
      f.write('\n'.join(lines))
    return "Going to Table NO %s" %uname  

  elif uname=="B": 
    lines = ["2"]
    with open('readme.txt', 'w') as f:
      f.write('\n'.join(lines))
    return "Going to Table NO %s" %uname  

  elif uname=="C": 
    lines = ["3"]
    with open('readme.txt', 'w') as f:
      f.write('\n'.join(lines))
    return "Going to Table NO %s" %uname  

  elif uname=="D": 
    lines = ["4"]
    with open('readme.txt', 'w') as f:
      f.write('\n'.join(lines))
    return "Going to Table NO %s" %uname  

  elif uname=="H":
    lines = ["0"]
    with open('readme.txt', 'w') as f:
      f.write('\n'.join(lines))
    return "Going to HOME" 

  else:
    return "Entered wrong table number"

       
if __name__ == '__main__':  
  app.run(debug = True)  