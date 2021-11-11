FROM node:latest

RUN npm install --global leasot

WORKDIR /code
VOLUME ["/code"]

ENTRYPOINT ["/usr/local/bin/leasot", "--tags", "@ERROR,@COMENTARIO", "-S"]
CMD ["--help"]
