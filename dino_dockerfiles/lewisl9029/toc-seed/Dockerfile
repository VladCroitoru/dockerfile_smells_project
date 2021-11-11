FROM node:0.10.40-slim

MAINTAINER Lewis Liu

WORKDIR /toc-seed

COPY telehash-v2 telehash-v2

# Expose telehash seed server port
EXPOSE 42424
EXPOSE 42424/udp

# Mount this as a volume to provide an existing keypair or generate a new one
VOLUME /toc-seed/config
CMD [ "node", "telehash-v2/seed.js", "--id", "/toc-seed/config/keypair.json" ]
