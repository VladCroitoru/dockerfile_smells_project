FROM node:8.11-alpine

RUN apk add --update git openssh gawk tzdata wget ca-certificates && \
  rm -rf /tmp/* /var/cache/apk/*

#make sure we get fresh keys
RUN rm -rf /etc/ssh/ssh_host_rsa_key /etc/ssh/ssh_host_dsa_key
RUN update-ca-certificates

CMD [ "/bin/ash" ]
