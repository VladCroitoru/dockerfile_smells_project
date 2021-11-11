FROM jeanblanchard/busybox-java:8

MAINTAINER Kamil Manka <kamil.manka@gmail.com>

ENV YOUTRACK_VERSION 6.0.12463
RUN mkdir -p /opt/youtrack
RUN wget -cq http://download.jetbrains.com/charisma/youtrack-$YOUTRACK_VERSION.jar -O /opt/youtrack/youtrack-$YOUTRACK_VERSION.jar
RUN ln -s /opt/youtrack/youtrack-$YOUTRACK_VERSION.jar /opt/youtrack/youtrack.jar

WORKDIR /opt/youtrack

ADD youtrack_run.sh /opt/youtrack/
ADD log4j.xml /opt/youtrack/
RUN chmod o+rx youtrack_run.sh

EXPOSE 8080

VOLUME ["/root"]

CMD ["./youtrack_run.sh"]