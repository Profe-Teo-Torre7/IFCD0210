from flask import Flask,render_template,abort,request,session,redirect,flash
import requests

app = Flask(__name__)
app.secret_key = "supersecreto"

API = "http://127.0.0.1:5002/api"

def get_posts():
    return requests.get(f"{API}/posts").json()
    
def get_posts_all():
    return requests.get(f"{API}/posts_all").json()

def get_post(post_id):
    resp = requests.get(f"{API}/post/{post_id}")
    if resp.status_code == 404:
        return None
    
    return resp.json()

def is_admin():
    return session.get('rol') == 'admin'

# ------------------------------------------

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


@app.route('/')
def home():
    entradas = get_posts()
    return render_template('home.html',posts=entradas)

@app.route('/post/<int:post_id>')
def post_detail(post_id):
    entrada = get_post(post_id)
    if entrada is None:
        abort(404)
    return render_template('post.html',post=entrada)

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        data = {
            'email':request.form['email'],
            'password': request.form['password']
        }
        
        response = requests.post(f"{API}/login",json=data)

        if response.status_code == 200:
            user = response.json()
            session['user_id'] = user['id']
            session['rol'] = user['rol']
            return redirect('/admin')
        else:
            flash('Credenciales incorrectas.')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

@app.route('/admin')
def admin():
    if not is_admin():
        return redirect('/login')
    
    entradas = get_posts_all()
    return render_template('admin.html',posts=entradas)



# --------------------------------------------
if __name__ == '__main__':
    app.run(port=5000,debug=True)