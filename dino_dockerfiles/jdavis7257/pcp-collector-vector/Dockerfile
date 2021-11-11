FROM ubuntu:trusty
MAINTAINER John Davis

RUN apt-get update &&\
    apt-get install -y curl apt-transport-https supervisor &&\
    curl 'https://bintray.com/user/downloadSubjectPublicKey?username=pcp' | sudo apt-key add - &&\
    echo "deb https://dl.bintray.com/pcp/trusty trusty main" | sudo tee -a /etc/apt/sources.list &&\
    apt-get update &&\
    apt-get install -y pcp pcp-webapi

ADD supervisor.conf /etc/supervisor/supervisord.conf

EXPOSE 44321 44323 44322

CMD /usr/bin/supervisord -c /etc/supervisor/supervisord.conf
