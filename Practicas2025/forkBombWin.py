import os
import time
import subprocess

while True:
    subprocess.Popen(["notepad.exe"])  # Abre una terminal en Linux
    time.sleep(0.5)  # Pequeña pausa para no colapsar el sistema de inmediato
