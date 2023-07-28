from flask import Flask, render_template, request
from nltk.chat.util import Chat, reflections
que1 = r'how are you' 
answer1 = [
    'all well',
    'I am good',
    'awesome'
]
que2 = r'what(.*)do(.*)'
answer2 = [
    'I can reply to your queries',
    'I am here to answer your questions',
    'I can chat with you'
]
que3 = r'(.*)your name'
answer3 = [
    'My name is chatty',
    'I am chatty'
]
que4 = r'(.*)mausam(.*)b[a]+rish(.*)'
answer4 = ['It look it will rain today', 'baarish ka mausam hai', 'baarish ho sakti hai mausam kharab hai']
qa_pair = [
    (que1 , answer1),
    (que2 , answer2),
    (que3 , answer3),
    (que4 , answer4)
]
chatbot = Chat(qa_pair)



app = Flask(__name__)
@app.route('/')
def home():
    global chatbot
    query = request.args.get('query')
    if query!=None:
        response = chatbot.respond(query)
        if response == None:
            response = 'Sorry i am not sure'

    else:
        response = "We didn't get the query"
    return render_template('index.html', result = response)
@app.route('/chatbot')
def chat():
    return "<h2>Chat Bot</h2>"
app.run(debug = True)