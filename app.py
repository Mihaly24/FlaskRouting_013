from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
   return 'Welcome, %s!' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      return render_template('login.html')  # Bagian yang diubah, yaitu memanggil html nya dengan render_template

if __name__ == '__main__':
   app.run(debug = True)