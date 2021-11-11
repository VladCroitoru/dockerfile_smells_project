FROM microsoft/dotnet:2.0.0-preview1-runtime

MAINTAINER nest.yt

ADD start-app.sh /etc/

# set up the packages
RUN apt-get update -y && \
    apt-get install -y sudo git jq && \
    apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \
    mkdir /usr/local/tree && \
    git clone https://github.com/inkton/nest.git /usr/local/tree/nest && \
    chmod +x /etc/start-app.sh

WORKDIR "/var/app"

CMD ["/etc/start-app.sh"]

EXPOSE 5000
