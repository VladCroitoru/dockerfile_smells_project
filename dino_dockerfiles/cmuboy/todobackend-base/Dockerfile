FROM java:8
MAINTAINER Joseph Ku <joseph.ku@octanner.com>

RUN curl -O http://downloads.typesafe.com/typesafe-activator/1.3.10/typesafe-activator-1.3.10-minimal.zip 
RUN unzip typesafe-activator-1.3.10-minimal.zip -d / && rm typesafe-activator-1.3.10-minimal.zip && chmod a+x /activator-1.3.10-minimal/bin/activator
ENV PATH $PATH:/activator-1.3.10-minimal/bin

ADD scripts/entrypoint.sh /usr/local/bin/entrypoint.sh
RUN chmod +x /usr/local/bin/entrypoint.sh
ENTRYPOINT ["entrypoint.sh"]
