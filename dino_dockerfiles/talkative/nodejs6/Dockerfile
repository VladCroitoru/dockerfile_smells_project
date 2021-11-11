FROM ubuntu:16.04
RUN apt-get update
RUN apt-get upgrade -y
COPY . /src
RUN chmod +x ./src/setup6.x
RUN ./src/setup6.x
RUN apt-get install -y nodejs
RUN node -v
