# Testing whether Hook is working or not.
# Double Check if Build is updating or not.
# Checking Display of SCM Message.
FROM node:0.10.44-slim

ADD . /home/demo/dv/

RUN cd /home/demo/dv && npm install

ENTRYPOINT ["/home/demo/dv/boot.sh"]
