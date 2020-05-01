import json
from .heap import Heap 
import pickle
def register_server():
    '''
    We Save All server instances here.
    Currently, Manually visit this function and append.
    A seperate endpoint to be exposed later.
    Currently , this returns a list of servers ordered in ascending order based on server load. 
    '''
    heap = Heap(10000)
    list_servers = pickle.load(open('server_list.pkl','rb'))
    list_servers.append({
        "url":"http://127.0.0.1:5000",
        "current_load":0,
        "is_active":True,
        "total_requests_served":0
    })
    heap.add(list_servers)
    heap.minHeap()
    list_servers = heap.heap
    pickle.dump(list_servers,open('server_list.pkl','wb'))

def get_server_list():
    '''
    This Returns Port Number of Server Instance with minimum load. 
    '''
    return pickle.load(open('server_list.pkl','rb'))
    

def min_loaded_server():
    '''
    This method will act as entry point while exposing endpoint to add servers.
    To be left blank for now.
    '''
    return get_server_list()[0]

def update_pickle():
    '''
    This method will re-pickelize server list, since we will have modified serve count, uptime, etc.
    '''
    pass