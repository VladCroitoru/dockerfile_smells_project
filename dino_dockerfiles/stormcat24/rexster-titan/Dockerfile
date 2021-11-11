FROM centos:centos6
MAINTAINER stormcat24 "a.yamada24@gmail.com"

# misc
RUN yum install -y unzip
RUN yum install -y java-1.7.0-openjdk

ADD http://tinkerpop.com/downloads/rexster/rexster-server-2.6.0.zip /
RUN unzip rexster-server-2.6.0.zip
RUN rm rexster-server-2.6.0.zip
RUN mv rexster-server-2.6.0 rexster-server
RUN mkdir -p rexster-server/ext/titan

ADD http://s3.thinkaurelius.com/downloads/titan/titan-0.5.2-hadoop2.zip /
RUN unzip titan-0.5.2-hadoop2.zip
RUN cp -R titan-0.5.2-hadoop2/lib/* rexster-server/ext/titan/
RUN rm -rf titan-0.5.2-hadoop2*

EXPOSE 8182 8183 8184
WORKDIR rexster-server
ENTRYPOINT ["bin/rexster.sh", "--start"]
