FROM ironsalsa/alpine-node-git
ENV YQ_VERSION=1.14.1
RUN apk add --update ca-certificates openssl && update-ca-certificates
RUN apk add --no-cache curl jq && npm install yaml-front-matter -g
RUN wget https://github.com/mikefarah/yq/releases/download/${YQ_VERSION}/yq_linux_amd64 && \ 
  mv yq_linux_amd64 /usr/bin/yq && \
  chmod +x /usr/bin/yq
CMD [ "/bin/ash" ]
