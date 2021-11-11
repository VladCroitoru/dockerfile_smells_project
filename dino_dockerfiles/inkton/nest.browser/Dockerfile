FROM microsoft/dotnet:runtime
MAINTAINER nest.yt

ADD start-app.sh /etc/
ADD load-db /usr/sbin/
ADD save-db /usr/sbin/

# set up the packages
RUN apt-get update -y && \
    apt-get install -y sudo git jq wget rsync python-pip python-dev build-essential vim inetutils-ping && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir /usr/local/tree && \
    git clone https://github.com/inkton/nest.git /usr/local/tree/nest && \
    chmod +x /etc/start-app.sh && \
    chmod +x /usr/sbin/load-db && \
    chmod +x /usr/sbin/save-db && \
    cd /usr/sbin/ && wget https://raw.githubusercontent.com/rabbitmq/rabbitmq-management/v3.7.0/bin/rabbitmqadmin && \
    chmod +x /usr/sbin/rabbitmqadmin
    
WORKDIR "/var/app"

CMD ["/etc/start-app.sh"]

