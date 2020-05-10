from Register import register
import pickle

ref = register.Register()
ref.register_server()
pickle.dump(ref, open('register.pkl', 'wb'))