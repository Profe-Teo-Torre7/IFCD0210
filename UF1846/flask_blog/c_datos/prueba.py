import requests

usr = {'nombre':'Teo',
    'email':'nada@nada.es',
    'pw_hash':'1234',
    'rol':'user',
    'f_alta':'2026-03-17'}


#resp = requests.post('http://127.0.0.1:5000/data/user',json=usr)
#print(resp)

resp = requests.get(
    'http://127.0.0.1:5000/data/user/by-email',
    params={'email':'nada@nada.es'})

print(resp.content.decode("utf-8"))