FROM jetty
MAINTAINER ndrouin
ENV LANG fr_FR.UTF-8

#change sh to bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh

#go home
WORKDIR /root
 
#install vim
RUN apt-get update -y
RUN apt-get install vim -y
ADD colors /etc/vim/colors
ADD vimrc.local /etc/vim

#install git
RUN apt-get install git -y

#install conscript
RUN PATH=$PATH:~/bin
RUN export PATH
RUN CONSCRIPT_HOME=/root
RUN export CONSCRIPT_HOME
RUN source ~/.bashrc
RUN wget https://raw.githubusercontent.com/foundweekends/conscript/master/setup.sh
RUN chmod +x setup.sh
RUN ./setup.sh

#install giter8
RUN /root/.conscript/bin/cs foundweekends/giter8

#get skeleton project
RUN /root/.conscript/bin/g8 scalatra/scalatra-sbt --organization=easywebsites --package=com.easywebsites.app --name=EasyWebsitesApp --servlet_name=ControllerServlet --scala_version=2.12.1 --sbt_version=0.13.13 --version=1.0 --scalatra_version=2.5.0

#compile project
WORKDIR /root/easywebsitesapp
RUN chmod u+x /root/easywebsitesapp/sbt
RUN /root/easywebsitesapp/sbt -batch -sbt-create
RUN ./sbt package
RUN cp /root/easywebsitesapp/target/scala-2.12/easywebsitesapp_2.12-1.0.war /var/lib/jetty/webapps/root.war

#get sources
WORKDIR /root
RUN git clone https://github.com/ndrouin/nlpf-tp2.git
#change default sources
RUN cp -rf /root/nlpf-tp2/src/ /root/easywebsitesapp/

#add run script
WORKDIR /root/easywebsitesapp
ADD run.sh /root/easywebsitesapp
RUN chmod +x run.sh

#install mongoDB
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6
RUN echo "deb http://repo.mongodb.org/apt/debian jessie/mongodb-org/3.4 main" | tee /etc/apt/sources.list.d/mongodb-org-3.4.list
RUN apt-get update
RUN apt-get install -y mongodb-org
RUN mkdir /srv/mongodb
ADD init.js /root

#default command
ADD entrypoint.sh /root
RUN chmod +x /root/entrypoint.sh
ENTRYPOINT /root/entrypoint.sh

#open firewall
EXPOSE 8080
