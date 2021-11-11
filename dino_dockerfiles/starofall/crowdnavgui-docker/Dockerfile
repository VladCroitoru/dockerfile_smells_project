FROM dorowu/ubuntu-desktop-lxde-vnc

# Install recent sumo
RUN apt-get update
RUN add-apt-repository ppa:sumo/stable
RUN apt-get update
RUN apt-get install -y sumo sumo-tools sumo-doc

# Creating desktop shortcut
RUN mkdir /home/ubuntu/Desktop
RUN echo "#!/bin/bash \n cd /app/ \n python ./run.py" > /home/ubuntu/Desktop/startGUI.sh
RUN chmod +x /home/ubuntu/Desktop/startGUI.sh

RUN apt-get install -y git
ENV SUMO_HOME /usr/share/sumo
RUN mkdir /app && git clone https://github.com/Starofall/CrowdNav.git /app
RUN python /app/setup.py install
