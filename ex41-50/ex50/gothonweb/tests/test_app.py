from app import app
from flask import request

MAIN_URL = "http://localhost/"

app.config['TESTING'] = True
web = app.test_client()

def test_index():
    rv = web.get("/")
    assert rv.status_code == 200
    assert b"<em>Hello</em>, world!" in rv.data

    data = {'greeting': "Dm cac ban"}
    rv = web.post("/", follow_redirects=True, data=data)
    assert rv.status_code == 200
    assert b'I just wanted to say <em style="color: green; font-size: 2em">Dm cac ban</em>.' in rv.data

def test_non_existing_route():
    rv = web.get("/test")
    assert rv.status_code == 404

def test_login():
    correct_username = 'admin'
    correct_password = '123'
    
    data = {'username': correct_username, 'password': correct_password[0]} # correct password is 123
    rv = web.post("/login", data=data)
    assert b'<strong>ERROR(S): </strong>Invalid username or password!' in rv.data

    data = {'username': correct_username, 'password': correct_password}
    rv = web.post("/login", follow_redirects=True, data=data)
    assert b'Loading...' in rv.data
    assert bytes('<meta http-equiv="refresh" content="1.5; url={}upload/admin"'.format(MAIN_URL), 'utf-8') in rv.data
##### OLD TEST FROM TEXT ##############
# def test_index():
#     rv = web.get('/test', follow_redirects=True)
#     assert rv.status_code == 404

#     rv = web.get('/', follow_redirects=True)
#     assert rv.status_code == 200
#     assert b"<em>Hello</em>, world!" in rv.data

    # data = {'greeting': "DM CAC BAN!"}
    # rv = web.post('/', follow_redirects=True, data=data)
    # assert b"DM CAC BAN!" in rv.data

    # rv = web.get('/hello', follow_redirects=True)
    # assert rv.status_code == 200
    # assert b"Fill Out This Form" in rv.data

    # data = {'name': 'Zed', 'greet': 'Hola'}
    # rv = web.post('/hello', follow_redirects=True, data=data)
    # assert b"Zed" in rv.data
    # assert b"Hola" in rv.data