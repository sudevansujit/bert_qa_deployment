import os
from flask import Flask, render_template
from flask import request


from transformers import pipeline
  

nlp_qa = pipeline('question-answering')

def Bert_QA(answer_text, question ):
    '''
    Takes a `question` string and an `answer` string and tries to identify 
    the words within the `answer` that can answer the question. Prints them out.
    '''
    answer = nlp_qa(context = answer_text, question = question)
    
    return answer['answer']

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
  
    if request.method == 'POST':
      form = request.form
      result = []
      bert_abstract = form['paragraph']
      question = form['question']
      result.append(form['question'])
      result.append(Bert_QA(question, bert_abstract))
      result.append(form['paragraph'])

      return render_template("index.html",result = result)

    return render_template("index.html")

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
