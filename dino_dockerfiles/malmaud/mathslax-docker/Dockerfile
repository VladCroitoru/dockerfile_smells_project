FROM debian:jessie

RUN apt-get update && apt-get install nodejs npm default-jre git curl -y
RUN apt-get install openjdk-7-jdk -y
WORKDIR /usr/bin
RUN ln -s nodejs node
WORKDIR /
RUN git clone https://github.com/colbygk/mathslax
WORKDIR /mathslax
RUN make install
ENV PORT 9999
EXPOSE 9999
CMD ["node", "server.js"]
