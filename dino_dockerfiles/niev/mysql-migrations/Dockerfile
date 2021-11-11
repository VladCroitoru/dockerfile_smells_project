FROM ubuntu:14.04

ADD http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.3.tar.gz mysql-connector-python-2.1.3.tar.gz
RUN tar xf mysql-connector-python-2.1.3.tar.gz && (cd mysql-connector-python-2.1.3 && python3 setup.py install && rm -rf mysql-connector-python-2.1.3)

VOLUME /migrations
COPY migrate.py /migrate.py
CMD /migrate.py
