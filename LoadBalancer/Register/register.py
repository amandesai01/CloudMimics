import sys

class Register():
    def __init__(self):
        self.list_servers = list()
        self.min_loaded_server = dict()
    
    def register_server(self):
        '''
        We Save All server instances here.
        Currently, Manually visit this function and append.
        A seperate endpoint to be exposed later.
        Currently , this returns a list of servers ordered in ascending order based on server load. 
        '''
        self.list_servers.append({
            "url":"http://127.0.0.1:5005/",
            "is_active":True,
            "total_requests_served":0
        })
        self.list_servers.append({
            "url":"http://127.0.0.1:5006/",
            "is_active":True,
            "total_requests_served":0
        })
        self.list_servers.append({
            "url":"http://127.0.0.1:5007/",
            "is_active":True,
            "total_requests_served":0
        })
        self.list_servers.append({
            "url":"http://127.0.0.1:5008/",
            "is_active":True,
            "total_requests_served":0
        })

        self.min_loaded_server = self.list_servers[0]

        self.update_min()
        return

    def reset_servers(self):
        for server in self.list_servers:
            server['total_requests_served'] = 0
        return

    def update_min(self):
        for server in self.list_servers:
            if server['total_requests_served'] < self.min_loaded_server['total_requests_served']:
                self.min_loaded_server = server
        return
    
    def get_min_loaded_server(self):
        server = self.min_loaded_server
        print(server)
        self.min_loaded_server['total_requests_served'] += 1
        self.update_min()
        return server