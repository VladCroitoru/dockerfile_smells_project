FROM java:8

MAINTAINER Juergen Jakobitsch <jakobitschj@semantic-web.at>
MAINTAINER Ivan Ermilov <ivan.s.ermilov@gmail.com>

ENV SOLR_VERSION="6.0.1"
ENV APPLICATION_ROOT="/usr/local/apache-solr"

RUN mkdir -p $APPLICATION_ROOT 
RUN cd $APPLICATION_ROOT && wget http://www-eu.apache.org/dist/lucene/solr/${SOLR_VERSION}/solr-${SOLR_VERSION}.tgz
RUN cd $APPLICATION_ROOT && tar zxvf solr-${SOLR_VERSION}.tgz
RUN ln -s $APPLICATION_ROOT/solr-${SOLR_VERSION} /usr/local/apache-solr/current
ENV SOLR_HOME=/usr/local/apache-solr/current
RUN cd $APPLICATION_ROOT && rm -f solr-${SOLR_VERSION}.tgz

ADD entrypoint.sh /entrypoint.sh
RUN chmod a+x /entrypoint.sh
ADD run.sh /run.sh
RUN chmod a+x /run.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/run.sh"]
