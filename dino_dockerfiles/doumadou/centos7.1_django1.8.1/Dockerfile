from doumadou/centos7.1_base:latest

COPY ./script /tmp/script

#RUN cd /tmp/script && chmod +x install.sh && ./install.sh
RUN cd /tmp/script && chmod +x install.sh && ls -ltr ./install.sh && sh ./install.sh && cd /tmp && rm -rf script
