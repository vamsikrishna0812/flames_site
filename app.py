from flask import Flask, render_template, url_for, request
from flames_package.flames_analyzer import flames_analyzer

flames = Flask(__name__)

@flames.route('/')
def hello():
    return render_template('index.html')

@flames.route('/flames', methods=['POST'])
def flames_fun():
    n1 = request.form.get('bfname')
    n2 = request.form.get('gfname')
    result = flames_analyzer(n1, n2)
    return render_template('flames.html', result=result, bfname = n1, gfname = n2)

if __name__ == '__main__':
    flames.run(debug=False)
