from flask import Flask, render_template, request, flash
import tokenizer
import stopWordRemover
import stemmer
import termWeighter
import codecs
app = Flask(__name__)
app.secret_key="sdaidjaidj"

lines=""
with codecs.open('SearchResults.txt', encoding='utf-8') as f:
    lines = f.read()
    f.close()

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/greet", methods=["POST", "GET"])
def greet():
    flash("Search Results for "
          +str(request.form['name_input']))
    with codecs.open('query.txt','a',encoding='utf-8') as f:
        f.truncate(0)
        f.write(str(request.form['name_input']))
        f.close();
    tokenizer.tokenizeQuery()
    stopWordRemover.remove_queryStopword()
    stemmer.stemQuery()
    yourList=[]
    cA = termWeighter.main()
    for i in range(10):
        with codecs.open(str(cA[i][0])+'.txt',encoding='utf-8')as f:
            lines = f.read()
            yourList.append(lines)
    print(len(cA))
    return render_template("index.html", your_list=yourList)

if __name__ == '__main__':
    app.run()
