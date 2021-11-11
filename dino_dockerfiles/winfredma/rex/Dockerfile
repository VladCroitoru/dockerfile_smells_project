FROM ubuntu:latest
USER root
RUN apt-get update
RUN apt-get install -y curl
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -
RUN apt-get update
RUN apt-get install -y nodejs
RUN npm -g install npm@latest
RUN ["/bin/bash", "-c", "npm -g install gulp"]
RUN ["/bin/bash", "-c", "npm -g install bower"]
ADD ./run.sh /root/run.sh
RUN chmod u+x /root/run.sh
CMD /root/run.sh
EXPOSE 3000