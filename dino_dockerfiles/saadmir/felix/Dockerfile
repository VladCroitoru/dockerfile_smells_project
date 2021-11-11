FROM mhart/alpine-node:8

RUN apk update
RUN apk upgrade
RUN apk add --no-cache --update python make gcc g++ tini dialog openssh-server
RUN rm  -rf /tmp/* /var/cache/apk/*

# ssh
ARG SSH_PASSWD="root:password"
RUN echo "$SSH_PASSWD" | chpasswd
COPY ./.ssh/sshd_config /etc/ssh/
RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key
RUN /usr/bin/ssh-keygen -A

EXPOSE 3000 2222

COPY . /app
WORKDIR /app

RUN rm -rf node_modules
RUN npm install

ENTRYPOINT ["/sbin/tini", "--"]
CMD nohup ./node_modules/.bin/gulp serve > nohup.log & /usr/sbin/sshd -D
