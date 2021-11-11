FROM java:8-jdk

ENV ORIENTDB_VERSION 2.1.5

RUN mkdir /orientdb && \
  wget -O orientdb-community-$ORIENTDB_VERSION.tar.gz "http://orientdb.com/download.php?email=unknown@unknown.com&file=orientdb-community-$ORIENTDB_VERSION.tar.gz&os=linux" \
  && tar -xvzf orientdb-community-$ORIENTDB_VERSION.tar.gz -C /orientdb --strip-components=1\
  && rm orientdb-community-$ORIENTDB_VERSION.tar.gz \
  && rm -rf /orientdb/databases/*

ENV PATH /orientdb/bin:$PATH

VOLUME ["/orientdb/backup", "/orientdb/databases", "/orientdb/config", "/orientdb/bin", "/orientdb/lib", "/orientdb"]

RUN touch /orientdb/log/server.log

WORKDIR /orientdb

#OrientDb binary
EXPOSE 2424

#OrientDb http
EXPOSE 2480

# Default command start the server
CMD ["server.sh"]
