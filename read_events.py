import subprocess

def open_terminal(command_template):
    topic_name = input("Enter the topic name: ")
    terminal_command = rf"cd C:\kafka && {command_template.format(topic_name=topic_name)}"
    subprocess.Popen(["start", "cmd", "/K", terminal_command], shell=True)

zookeeper_command_template = r".\bin\windows\kafka-console-consumer.bat --topic {topic_name} --from-beginning --bootstrap-server localhost:9092"
open_terminal(zookeeper_command_template)
