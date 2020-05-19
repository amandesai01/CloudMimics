import pickle
from ping3 import ping
import time

def check_servers():
    while True:
        register = pickle.load(open('register.pkl', 'rb'))
        servers = register.list_servers
        for server in servers:
            '''
            Skipping Checks for inactive servers, they will be checked separately.
            This is done to maintain uptime count and resets of all shards.
            '''
            if not server['is_active']:
                continue
            if not ping(server['url']):
                server['is_active'] = False
        pickle.dump(register, open('register.pkl', 'wb'))
        time.sleep(2.5)

check_servers()