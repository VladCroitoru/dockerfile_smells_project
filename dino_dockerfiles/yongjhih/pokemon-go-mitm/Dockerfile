FROM node

WORKDIR /src

ADD . /src

RUN apt-get update && \
    apt-get install -y libprotobuf-dev && \
    npm install && \
    npm install -g coffee-script && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

CMD ["npm", "start"]
