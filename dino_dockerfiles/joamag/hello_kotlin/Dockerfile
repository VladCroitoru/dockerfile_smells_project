FROM hivesolutions/alpine_dev:latest

LABEL version="1.0"
LABEL maintainer="João Magalhães <joamag@gmail.com>"

EXPOSE 8080

ENV HOST 0.0.0.0
ENV PORT 8080
ENV GRADLE_VERSION 4.3.1

ADD . /app

WORKDIR /app

RUN rm -rf /app/.git
RUN apk update && apk add openjdk8
RUN wget https://services.gradle.org/distributions/gradle-$GRADLE_VERSION-bin.zip && unzip gradle-$GRADLE_VERSION-bin.zip
RUN ln -s $(pwd)/gradle-$GRADLE_VERSION/bin/gradle /usr/bin/gradle
RUN gradle -Dorg.gradle.daemon=false -Dorg.gradle.parallel=false -Dkotlin.incremental=false -Dkotlin.compiler.execution.strategy="in-process" build

CMD ["gradle", "run"]
