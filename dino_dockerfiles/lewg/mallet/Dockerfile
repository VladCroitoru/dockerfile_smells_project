FROM java:8
ADD . /usr/src/mallet
WORKDIR /usr/src/mallet
RUN apt-get update && apt-get install -y make
RUN make
CMD bin/mallet
