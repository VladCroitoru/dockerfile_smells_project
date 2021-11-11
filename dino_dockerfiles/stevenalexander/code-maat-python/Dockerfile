# Base docker image
FROM pandeiro/oracle-jdk8
MAINTAINER Steven Alexander <steven.william.alexander@googlemail.com>

ENV LEIN_ROOT true

RUN wget -q -O /usr/bin/lein \
    https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein \
    && chmod +x /usr/bin/lein

RUN apt-get update
RUN apt-get install -y git 
RUN apt-get install -y python2.7
RUN apt-get install -y cloc

RUN mkdir /app
WORKDIR /app

RUN git clone https://github.com/adamtornhill/code-maat.git
WORKDIR code-maat

RUN /usr/bin/lein uberjar

WORKDIR target
# Rename the standalone jar to be version independant for the future
RUN find . -name '*standalone*' -exec bash -c 'mv $0 codemaat-standalone.jar' {} \;

RUN echo "alias maat='java -jar /app/code-maat/target/codemaat-standalone.jar'" >> /root/.bashrc
RUN echo "alias python='python2.7'" >> /root/.bashrc

ENTRYPOINT ["bash"]
