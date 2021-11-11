FROM ubuntu:18.04
RUN apt update -y && \
    apt install apache2 -y && \
    apt install g++ -y && \
    apt install libtool libqtgui4 libqtcore4 libcgicc-dev libqt4-xml libqt4-test libqt4-script libqt4-network libqt4-dbus libgle3 -y && \
    apt install libcgicc3 -y && \
    apt install libboost-all-dev -y && \
    apt install libmysqlclient-dev libmysqlcppconn-dev -y && \
    apt install make -y

COPY index.html /var/www/html/
COPY favicon.ico /var/www/html/
COPY src/* /var/www/html/src/

COPY conf/apache2.conf /etc/apache2/
COPY conf/cgid.conf /etc/apache2/mods-enabled/
COPY conf/cgid.load /etc/apache2/mods-enabled/
COPY conf/cgi.load /etc/apache2/mods-enabled/

RUN mkdir /var/www/cgi-bin/
COPY Makefile /var/www/cgi-bin/
COPY script.cpp /var/www/cgi-bin/
COPY text.cpp /var/www/cgi-bin/
COPY getdb.cpp /var/www/cgi-bin/
COPY getdb.h /var/www/cgi-bin/
COPY plagiarism.cpp /var/www/cgi-bin/

WORKDIR /var/www/cgi-bin
RUN make
RUN chmod 755 script.cgi
RUN chmod 755 text.cgi
RUN rm Makefile script.cpp text.cpp getdb.cpp plagiarism.cpp
CMD apache2ctl -D FOREGROUND
VOLUME ["/var/lock/"]