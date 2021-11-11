FROM node:latest
MAINTAINER ifelsemonkey@gmail.com

# Seems that I am compelled to have this as separate RUN commands
RUN apt-get update && apt-get install -y --no-install-recommends apt-transport-https\
    && wget -q -O - https://packages.cloudfoundry.org/debian/cli.cloudfoundry.org.key | apt-key add -\
    && echo "deb http://packages.cloudfoundry.org/debian stable main" | tee /etc/apt/sources.list.d/cloudfoundry-cli.list

RUN apt-get update && apt-get install -y --no-install-recommends\
    vim\
    hexedit\
    tmux\
    unzip\
    less\
    xmlstarlet\
    jq\
    #cf-cli\
    #openssh-server\
    net-tools
    #xauth\
    #libgtk2.0-0\
    #libxss1\
    #libgconf-2-4\
    #libnss3-dev\
    #libasound2\
    #libxtst6\ 
    #&& npm install -g @angular/cli@latest\
    #&& npm install -g gulp\
    #&& npm install -g typescript\
    #&& mkdir /root/bin /root/src && cd /root/src
    #&& mkdir /opt/vscode /opt/vscode-datadir
    #&& git clone https://github.com/ifelsemonkey/mycli.git
    #&& cd mycli\
    #&& ./setup.sh

#RUN wget https://go.microsoft.com/fwlink/?LinkID=620884 --output-document=/root/vscode.tar.gz && tar xvzpf /root/vscode.tar.gz -C /opt/vscode\ 
#    && rm -f /root/vscode.tar.gz

#RUN echo "export PATH=/root/bin:$PATH" >> ~/.bashrc
    #&& echo "alias vscode='/opt/vscode/VSCode-linux-x64/bin/code --user-data-dir=/opt/vscode-datadir'" >> ~/.bashrc\
    #&& echo "root:password" | /usr/sbin/chpasswd\
    #&& sed -i -e 's/Port 22/Port 2222/' -e 's/\(PermitRootLogin\).*/\1 yes/' /etc/ssh/sshd_config\
    #&& echo "X11UseLocalhost no" >> /etc/ssh/sshd_config\
    #&& mkdir /var/run/sshd

WORKDIR /root

#ENTRYPOINT ["/usr/sbin/sshd","-D"]
