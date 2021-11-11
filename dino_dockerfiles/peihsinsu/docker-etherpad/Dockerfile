FROM node

RUN apt-get update -y && apt-get install gzip git curl python libssl-dev pkg-config build-essential -y
RUN git clone git://github.com/ether/etherpad-lite.git app

WORKDIR /app

CMD ["./bin/run.sh", "--root"]
