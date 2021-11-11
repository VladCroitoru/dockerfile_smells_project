from openjdk:8

MAINTAINER Matthijs van den Bos <matthijs@vandenbos.org>

ENV TARGET_DIR="/usr/local/lib/javaqa" \
    GRADLE_HOME="/usr/local/lib/javaqa/gradle-3.0" \
    PATH="/usr/local/lib/javaqa/gradle-3.0/bin:${PATH}"

RUN mkdir -p $TARGET_DIR

WORKDIR $TARGET_DIR

COPY usage.txt $TARGET_DIR

RUN wget https://services.gradle.org/distributions/gradle-3.0-bin.zip -O gradle.zip
RUN unzip gradle.zip -d /usr/local/lib/javaqa
RUN rm gradle.zip

CMD cat $TARGET_DIR/usage.txt
