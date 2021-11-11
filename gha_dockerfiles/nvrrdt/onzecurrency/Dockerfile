FROM ubuntu:focal
WORKDIR /onzecurrency
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y git g++ cmake wget python3-virtualenv libboost-all-dev libssl-dev \
                                                                        librocksdb-dev libminiupnpc-dev libsnappy-dev \
                                                                        curl libpthread-stubs0-dev libsecp256k1-dev ninja-build build-essential \
                                                                        libgcrypt-dev
RUN virtualenv -p /usr/bin/python3 .venv && . ./.venv/bin/activate
#CMD [ "whoami" ]
#CMD [ "ls", "-al", "/libcrowd" ]
CMD [ "python3", "./scripts/build.py" ]