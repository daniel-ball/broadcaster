from flask import Flask, render_template, request
from webexteamssdk import WebexTeamsAPI

app = Flask(__name__)

api = WebexTeamsAPI(access_token='YOUR_ACCESS_TOKEN')

@app.route('/')
def home():
    try:
        person = api.people.me()
        pic = person.avatar
        
        rooms = api.rooms.list()
        for room in rooms:
            roomba = rooms[::]
            print(roomba)
            print(pic)

    except ApiError as e:
        print(e)

    return render_template('home.html', roomba=roomba, pic=pic)


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        roomList = request.form.getlist('rooms')
        comments = request.form['comments']
        print(roomList)
        print(comments)
    try:
        room_id_list = roomList
        for room_list in room_id_list:    
            message = api.messages.create(room_list, text=comments)
        print("New message created, with ID:", message.id)
        print(message.text)
    except ApiError as e:
        print(e)
    
    
    return render_template('success.html', roomList=roomList, comments=comments)

if __name__ == '__main__':
    app.run(debug=True) 