FROM ubuntu:14.04
MAINTAINER levkov
ENV DEBIAN_FRONTEND noninteractive
ENV NOTVISIBLE "in users profile"
RUN locale-gen en_US.UTF-8

RUN apt-get update && apt-get upgrade -y &&\
    apt-get install apt-transport-https -y &&\
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
#------------------------------Supervisor------------------------------------------------
RUN apt-get update && apt-get install -y supervisor && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir -p /var/log/supervisor    
COPY conf/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
EXPOSE 9001
CMD ["/usr/bin/supervisord"]
#---------------------------SSH---------------------------------------------------------
RUN apt-get update && apt-get install -y openssh-server && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN mkdir -p /var/run/sshd    
RUN sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd
ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile
COPY conf/sshd.conf /etc/supervisor/conf.d/sshd.conf

RUN echo 'root:ContaineR' | chpasswd
# -----------------------------------Java--------------------------------------
# RUN apt-get update && apt-get install software-properties-common -y && add-apt-repository ppa:webupd8team/java -y &&  apt-get update && \
#    echo debconf shared/accepted-oracle-license-v1-1 select true | debconf-set-selections && \
#    echo debconf shared/accepted-oracle-license-v1-1 seen true | debconf-set-selections && \
#    apt-get install oracle-java8-installer -y && \
#    rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
#--------------------------------Servers------------------------------------------
RUN apt-get update && apt-get -y install mysql-server-5.5 dos2unix && \ 
    rm -rf /var/lib/apt/lists/* && rm -rf /tmp/*
ADD conf/mysql.conf /etc/supervisor/conf.d/   
#---------------------------------------------------------------------------------
RUN mkdir -p /install
COPY install/install.sh /install/install.sh
RUN cd /install && dos2unix *
COPY install/mysql-connector-java-5.1.38-bin.jar /install/mysql-connector-java-5.1.38-bin.jar
RUN cd /install && wget https://dl.dropboxusercontent.com/u/6229500/nolio_server_linux-x64_6_0_0_b511.sh 
RUN chmod +x /install/nolio_server_linux-x64_6_0_0_b511.sh && chmod +x /install/install.sh
RUN /bin/bash -c "/usr/bin/mysqld_safe &" && \ 
    sleep 5 && \
    mysql -e "SET PASSWORD FOR 'root'@'localhost' = PASSWORD('123456');" && \
    cd /install && ./install.sh && \
    rm -rf /install/install.sh && rm -rf /install/nolio_server_linux-x64_6_0_0_b511.sh
EXPOSE 8080 6600 6900

COPY install/dfg.sh /usr/local/bin/dfg.sh
RUN cd /usr/local/bin && dos2unix dfg.sh
RUN chmod +x /usr/local/bin/dfg.sh 
  

