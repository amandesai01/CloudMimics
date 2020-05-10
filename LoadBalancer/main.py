from flask import Flask, redirect
import pickle

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def balancer(path):
    register = pickle.load(open('register.pkl', 'rb'))
    url = register.get_min_loaded_server()['url']
    pickle.dump(register, open('register.pkl', 'wb'))
    return redirect(url)
    
if __name__ == '__main__':
    app.run(port=4999, debug=True)
    