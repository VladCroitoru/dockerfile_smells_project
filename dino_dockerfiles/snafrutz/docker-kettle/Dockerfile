FROM java:latest
MAINTAINER snafrutz <piermarco.zerbini@gmail.com>
RUN apt-get install wget bash

# Install Kettle
RUN mkdir /kettle && \
    cd /kettle && \
    wget --quiet "https://downloads.sourceforge.net/project/pentaho/Data%20Integration/7.0/pdi-ce-7.0.0.0-25.zip" && \
    unzip pdi-ce-7.0.0.0-25.zip && \
    rm -f pdi-ce-7.0.0.0-25.zip

# Import ETL
RUN mkdir /etl

VOLUME [ "/etl" ]
ENTRYPOINT ["bash"]
WORKDIR /tmp
