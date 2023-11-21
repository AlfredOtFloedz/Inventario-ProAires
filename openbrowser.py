import webbrowser
import threading
import subprocess
import time 

subprocess.Popen(["python","manage.py", "runserver"])
    
time.sleep(0.5)
    
webbrowser.open("http://localhost:8000")
