FROM node:0.10.44-slim

ADD . /home/demo/box/

RUN cd /home/demo/box && npm install

ENTRYPOINT ["/home/demo/box/boot.sh"]
