import subprocess
import time


def open_terminal(command):
    terminal_command = rf"cd C:\kafka && {command}"
    subprocess.Popen(["start", "cmd", "/K", terminal_command], shell=True)


zookeeper_command = r".\bin\windows\zookeeper-server-start.bat .\config\zookeeper.properties"
kafka_command = r".\bin\windows\kafka-server-start.bat .\config\server.properties"

open_terminal(zookeeper_command)
time.sleep(18)
open_terminal(kafka_command)
