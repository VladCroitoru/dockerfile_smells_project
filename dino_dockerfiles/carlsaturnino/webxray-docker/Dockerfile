FROM micktwomey/python3.4:latest
MAINTAINER Carl Saturnino <cosaturn@gmail.com>

RUN apt-get update
RUN apt-get -y install phantomjs
RUN apt-get -y --fix-missing install mysql-server
RUN apt-get -y install wget
RUN python3 --version
RUN pip install --upgrade pip
RUN wget -O /tmp/mysql-connector-python-2.0.4.tar.gz https://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.0.4.tar.gz
RUN cd /tmp && \
    tar -xvf mysql-connector-python-2.0.4.tar.gz && \
    cd mysql-connector-python-2.0.4/ && \
    python3 setup.py install && \
    cd

RUN git clone https://github.com/timlib/webXray.git
RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
COPY start.sh /
COPY url.lst /webXray/page_lists
WORKDIR /webXray
ENTRYPOINT ["/start.sh"] 

