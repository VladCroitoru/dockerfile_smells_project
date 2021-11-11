FROM adoptopenjdk/openjdk8:latest

RUN apt-get update
RUN apt-get install -y ca-certificates uuid-runtime git

ADD https://cli.run.pivotal.io/stable?release=linux64-binary /tmp/cf-cli.tgz

RUN mkdir -p /usr/local/bin && \
    tar -xzf /tmp/cf-cli.tgz -C /usr/local/bin && \
    cf --version

RUN java -version
