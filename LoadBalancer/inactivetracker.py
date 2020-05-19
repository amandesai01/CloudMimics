import pickle
from ping3 import ping
import time

def check_servers():
    while True:
        register = pickle.load(open('register.pkl', 'rb'))
        servers = register.list_servers
        for server in servers:
            '''
            Performing checkes for inactive server.
            If they become active, reset count for all servers.
            '''
            if not server['is_active']:
                if ping(server['url']):
                    server['is_active'] = True
            register.reset_servers()
        pickle.dump(register, open('register.pkl', 'wb'))
        time.sleep(2.5)

check_servers()