from flask import Flask, render_template,url_for,request
import openai


app = Flask(__name__,template_folder="templates")

with open("C://Users//student//Documents//chatgptkey.txt","r") as file:
    openai.api_key=file.read().strip()


conversation_history = []
conversation_history1 = []
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    conversation_history.append({"role": "user", "content": user_input})
    conversation_history1.append({"role": "User", "content": user_input})


    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation_history
    )
    chatbot_response = response.choices[0].message["content"]
    conversation_history.append({"role": "assistant", "content": chatbot_response})
    conversation_history1.append({"role": "Assistant", "content": chatbot_response})

    return render_template('index.html', user_input=user_input, conversation_history=conversation_history1)

if __name__ == '__main__':
    app.run(debug=True)


