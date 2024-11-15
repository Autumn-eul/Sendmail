from flask import Flask, url_for, make_response, render_template, request, redirect
import urllib.parse

app = Flask(__name__)

# 메일 전송 폼이 보이는 기능 구현
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods = ['GET', 'POST'])
def contect_complete():
    if request.method == 'POST':
        
        return redirect('contact_complete')
    
    return render_template('contact_complete.html')

if __name__ == "__main__":
    app.run(debug=True)