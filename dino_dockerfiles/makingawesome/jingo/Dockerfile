FROM mhart/alpine-node:latest
ADD . /opt/jingo
WORKDIR /opt/jingo
RUN git config --global user.name "Jingo Wiki" && git config --global user.email "everyone@jingo" && npm install
CMD /bin/bash /opt/jingo/start.sh
