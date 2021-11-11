FROM debian:jessie-slim
MAINTAINER Jonathan Delfour

# Oracle Instant Client layer
COPY oracle_install/* /tmp/

#download from http://www.oracle.com/technetwork/topics/linuxx86-64soft-092277.html
RUN apt-get update && apt-get install -y alien && \
    alien -iv /tmp/oracle-instantclient12.2-basiclite-12.2.0.1.0-1.x86_64.rpm && \
    alien -iv /tmp/oracle-instantclient12.2-devel-12.2.0.1.0-1.x86_64.rpm && \
    apt-get purge -y alien perl perl5 && apt-get -y autoremove && apt-get clean && \
    rm -rf /tmp/oracle-* && rm -rf /usr/share/docs && rm -rf /usr/share/man 

# Environment variables
ENV ORACLE_HOME=/usr/lib/oracle/12.2/client64
ENV LD_LIBRARY_PATH=$ORACLE_HOME/lib
ENV PATH=$ORACLE_HOME/bin:$PATH

# Python3 + cx_Oracle layer 
RUN apt-get install -y python3 python3-dev python3-pip libaio1 && \
    pip3 install cx_Oracle

# install any extra requirements required by some apps
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

RUN rm -rf /usr/share/doc && rm -rf /usr/share/man && \
    apt-get purge -y python3-dev python3-pip && apt-get clean

# Application layer
#COPY app/ /home
WORKDIR /home

CMD ["/bin/bash"]