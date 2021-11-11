FROM ubuntu

RUN apt-get update -y
ENV MYSQL_ADMIM  ""
ENV MYSQL_ADMINPASS ""
ENV MYSQL_HOST ""
ENV MYSQL_DBNAME ""
ENV MYSQL_PASSWORD ""
ENV MYSQL_USER ""
ENV MYSQL_OUTPUT_TYPE ""
ENV INSTALLDB "false"
ENV DELETEDB "false"
ENV ADD_DBUSER "false"
ENV WALDO_FILE ""
ENV ARCHIVE_DIR ""
ENV FILE_BASE ""
ENV SPOOL_DIR ""
ENV ONLY_NEW_EVENT ""

RUN DEBIAN_FRONTEND=noninteractive apt-get install -y  build-essential autoconf autogen m4 libtool libpcap-dev bison flex  libmysqlclient-dev mysql-client libdumbnet-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y mysql-client git vim tcpflow wireshark p0f wget tzdata python-jinja2

# Compile tcl without multithread
# apt-get install -y devscripts dpkg-dev zlib1g-dev debhelper
# apt-get source tcl8.6 ; apt-get build-dep tcl
# vim debian/rules ; replace --enable-threads by --disable-threads
# vim debian//libtcl8.6.symbols ; remove Tcl_GetMemoryInfo and notifierInitMutex@Base 8.6.5 and  notifierMutex@Base 8.6.5
# debuild -us -uc
# cd .. ; dpkg -i tcl*
WORKDIR /opt/
COPY barnyard-conf.template /opt/
COPY entrypoint.sh /opt/
COPY jinja-barnyard-conf.py /opt/

COPY ./snort-conf/ /etc/snort/
RUN mkdir /var/log/snort

RUN ln -s /usr/include/dumbnet.h /usr/include/dnet.h
RUN ldconfig
ENV DAQ_VERSION 2.0.6
RUN wget https://www.snort.org/downloads/snort/daq-${DAQ_VERSION}.tar.gz \
    && tar xvfz daq-${DAQ_VERSION}.tar.gz \
    && cd daq-${DAQ_VERSION} \
	    && ./configure; make; make install

RUN mkdir /var/log/barnyard2
RUN git clone https://github.com/firnsy/barnyard2.git 
RUN cd /opt/barnyard2/ && bash /opt/barnyard2/autogen.sh && \
	bash /opt/barnyard2/configure --with-mysql --with-mysql-libraries=/usr/lib/x86_64-linux-gnu && \
	make && make install
RUN chmod +x /opt/entrypoint.sh
ENTRYPOINT ["/opt/entrypoint.sh"]
