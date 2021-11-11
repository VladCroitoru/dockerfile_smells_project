FROM java:openjdk-8u111-jdk

LABEL maintainer="Wadjetz <egor.neon@gmail.com>"

RUN curl -sL https://deb.nodesource.com/setup_9.x | bash - && \
    apt-get install -y nodejs bc && \
    wget -nv http://dl.bintray.com/sbt/debian/sbt-1.0.3.deb && \
    dpkg -i sbt-1.0.3.deb && \
    wget -nv http://www.scala-lang.org/files/archive/scala-2.12.4.deb && \
    dpkg -i scala-2.12.4.deb && \
    rm sbt-1.0.3.deb scala-2.12.4.deb && \
    sbt --version \
    apt-get clean

CMD sbt
