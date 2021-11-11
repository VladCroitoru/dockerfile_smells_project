FROM arm32v7/node:10

ARG CNCJS_VER

RUN npm install -g cncjs@$CNCJS_VER --unsafe-perm
RUN apt-get update
RUN apt-get install -y udev
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
CMD ["/usr/local/bin/cnc"]

