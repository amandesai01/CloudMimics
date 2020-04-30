import json
from heap import Heap 
def get_server_list():
    '''
    We Save All server instances here.
    Currently, Manually visit this function and append.
    A seperate endpoint to be exposed later. 
    '''
    list_servers = list()
    list_servers.append({
        "url":"http://127.0.0.1:5000",
        "current_load":0,
        "is_active":True,
        "total_requests_served":0
    })
    return list_servers

def min_loaded_server():
    '''
    This Returns Port Number of Server Instance with minimum load.
    '''
    pass

def register_server():
    '''
    This method will act as entry point while exposing endpoint to add servers.
    To be left blank for now.
    '''
    pass
