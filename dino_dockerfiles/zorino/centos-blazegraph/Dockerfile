# Linux OS
FROM centos:centos7

# Maintainer
MAINTAINER zorino <maximilien1er@gmail.com>

# Install Java
RUN yum install -y java sysstat && yum clean all

# Create volume for graph data
RUN mkdir /mnt/graphs
VOLUME /mnt/graphs
WORKDIR /mnt/graphs
ENV GRAPH_HOME /mnt/graphs

# Install bigdata bundled (blazegraph) + utils
RUN mkdir -p /opt/blazegraph/utils
ENV PATH /opt/blazegraph/utils/:$PATH

RUN curl -L http://sourceforge.net/projects/bigdata/files/bigdata/1.5.3/bigdata-bundled.jar -o /opt/blazegraph/bigdata-bundled.jar

ADD RWStore.properties /opt/blazegraph/
ADD utils/load-graph.sh /opt/blazegraph/utils/
ADD utils/start-blazegraph.sh /opt/blazegraph/utils/

RUN chmod -R 755 /opt/blazegraph/

# Exec on start
ENTRYPOINT ["start-blazegraph.sh", "4g"]

# Expose Default Port
EXPOSE 9999
