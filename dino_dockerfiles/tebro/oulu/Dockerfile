FROM debian:8.2

# all external dependencies
RUN apt-get update && \
	apt-get upgrade -y && \	
	apt-get install curl unzip ruby git ruby-dev cmake g++ libssl-dev openssl -y && \
    gem install bundler

# setting up our friendly user developer - setting up user take 1/2
ENV UID=1000
ENV GID=1000
RUN mkdir -p /home/developer && \
    mkdir -p /etc/sudoers.d/ && \
    echo "developer:x:${UID}:${GID}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
    echo "developer:x:${UID}:" >> /etc/group && \
    echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
    chmod 0440 /etc/sudoers.d/developer

ADD . /opt/oulu
RUN (cd /opt/oulu && bundle install) && \
    chown -R developer /opt/oulu
EXPOSE 5000

# ending points - setting up user take 2/2
RUN chown ${UID}:${GID} -R /home/developer
USER developer
ENV HOME /home/developer
WORKDIR /opt/oulu/

CMD [ "foreman", "start" ]
