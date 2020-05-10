from flask import Flask, redirect
import pickle
from ping3 import ping
import time

app = Flask(__name__)

def check_servers():
    while True:
        register = pickle.load(open('register.pkl', 'rb'))
        servers = register.list_servers
        for server in servers:
            if not ping(server['url']):
                server['is_active'] = False
        pickle.dump(register, open('register.pkl', 'wb'))
        time.sleep(2.5)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def balancer(path):
    register = pickle.load(open('register.pkl', 'rb'))
    url = register.get_min_loaded_server()['url']
    pickle.dump(register, open('register.pkl', 'wb'))
    return redirect(url)
    
if __name__ == '__main__':
    app.run(port=4999, debug=True)
    