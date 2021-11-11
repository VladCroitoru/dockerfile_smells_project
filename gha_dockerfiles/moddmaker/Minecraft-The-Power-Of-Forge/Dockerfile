FROM ubuntu:latest
ENTRYPOINT [ "/bin/bash", "-l", "-c" ]

CMD [ "echo","apt","cd","ls","la","export" ]

CMD apt update -y 
CMD apt upgrade -y
CMD apt install maven -y 
CMD apt install openjdk-16-jdk -y 
CMD apt install curl -y 
CMD apt install tar -y 
CMD apt install wget -y 
CMD apt install vim -y
CMD apt install python3 -y
CMD apt install python3-pip -y 
CMD apt install zip -y
CMD apt install build-essential manpages-dev -y
CMD apt install p7zip -y
CMD apt install npm -y 
CMD apt install nodejs
CMD apt install git 
CMD apt install mono-complete
CMD apt install cmake -y 
CMD apt install make -y 
CMD apt install build-essential manpages-dev -y
CMD git clone https://github.com/moddmaker/Minecraft-The-Power-Of-Forge.git
CMD apt install python3-flask
CMD export FLASK_ENV=development

ENV HOME /root
ADD . $HOME
ENV JAVA_HOME /usr/lib/jvm/java-16-openjdk-armhf
ADD . $JAVA_HOME
ENV M2_HOME /usr/share/maven
ADD . $M2_HOME
ENV FLASK_APP Minecraft-The-Power-Of-Forge/src/master/languages/com/moddmaker/minecraftthepowerofforge/animation.py
ADD . $FLASK_APP
ENV PATH $HOME/bin:$FLASK_APP:$JAVA_HOME/bin:$M2_HOME/bin
ADD . $PATH

CMD echo $JAVA_HOMR
CMD echo $M2_HOME
CMD echo $PATH
