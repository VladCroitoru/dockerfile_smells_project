FROM ubuntu
RUN apt update && apt autoremove
RUN apt -y install sudo curl dirmngr apt-transport-https lsb-release ca-certificates
RUN curl -sL https://deb.nodesource.com/setup_14.x | sudo -E bash -
RUN sudo apt -y install nodejs
RUN apt-get -y install git
RUN apt-get -y install vim
CMD sh /var/app/buildInDocker.sh > /var/log.txt
