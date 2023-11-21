import webbrowser
import threading
import subprocess
import time 

def open_browser():
    subprocess.Popen(["python","manage.py", "runserver"])
    
    time.sleep(2)
    
    webbrowser.open("localhost:8000")
    
if __name__ == "__main__":
    server_thread = threading.Thread(target=open_browser)
    server_thread.start
    
    