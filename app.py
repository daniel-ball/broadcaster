"""
Copyright (c) 2020 Daniel Ball

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

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
