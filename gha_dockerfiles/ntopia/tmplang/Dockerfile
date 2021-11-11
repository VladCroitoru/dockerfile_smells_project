FROM docker.io/adoptopenjdk/openjdk11:x86_64-debian-jdk-11.0.12_7

RUN apt update && apt -y install unzip gcc g++ pkg-config uuid-dev git cmake vim

WORKDIR /usr/local/lib

RUN curl -O https://www.antlr.org/download/antlr-4.9.2-complete.jar

ENV CLASSPATH="/usr/local/lib/antlr-4.9.2-complete.jar"
RUN echo 'alias antlr4="java -jar /usr/local/lib/antlr-4.9.2-complete.jar"' >> ~/.bashrc
RUN echo 'alias grun="java org.antlr.v4.gui.TestRig"' >> ~/.bashrc
ENV LD_LIBRARY_PATH="/usr/local/lib:${LD_LIBRARY_PATH}"

WORKDIR /tmp/antlr4

RUN curl -O https://www.antlr.org/download/antlr4-cpp-runtime-4.9.2-source.zip
RUN unzip antlr4-cpp-runtime-4.9.2-source.zip

RUN mkdir build && mkdir run
WORKDIR /tmp/antlr4/build

RUN cmake .. -DANTLR_JAR_LOCATION=/usr/local/lib/antlr-4.9.2-complete.jar
RUN make
RUN DESTDIR= make install

WORKDIR /work
ENTRYPOINT ["/bin/sh", "-c", "/bin/bash"]
