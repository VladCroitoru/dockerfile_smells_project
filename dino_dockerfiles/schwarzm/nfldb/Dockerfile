FROM python:2.7
ADD http://burntsushi.net/stuff/nfldb/nfldb.sql.zip nfldb.sql.zip
RUN apt-get -q update && apt-get -qy install unzip postgresql-client
RUN unzip nfldb.sql.zip
RUN pip2 install nfldb
ADD config.ini /root/.config/nfldb/config.ini
ADD start.sh /start.sh
RUN chmod 700 /start.sh
ENTRYPOINT /start.sh
