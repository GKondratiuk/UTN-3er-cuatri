import os
import time
import subprocess

while True:
    subprocess.Popen(["x-terminal-emulator"])  # Abre una terminal en Linux
    time.sleep(0.5)  # Pequeña pausa para no colapsar el sistema de inmediato
