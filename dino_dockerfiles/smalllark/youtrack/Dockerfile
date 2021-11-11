FROM smalllark/java
MAINTAINER Dmitri Sh <smalllark@gmail.com>

# Install Youtrack.
ENV YOUTRACK_VERSION 2018.2.43142
RUN mkdir -p /usr/local/youtrack && \
    mkdir -p /var/lib/youtrack && \
    wget -nv https://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar -O /usr/local/youtrack/youtrack-$YOUTRACK_VERSION.jar && \
    ln -s /usr/local/youtrack/youtrack-$YOUTRACK_VERSION.jar /usr/local/youtrack/youtrack.jar
ADD ./etc /etc
EXPOSE 8080

CMD ["/sbin/my_init"]

# Clean up APT when done.
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
