FROM java:openjdk-7u65-jdk
# maintainers details
# system installations
RUN apt-get update && apt-get install -y wget 
# product installations
RUN wget 'http://www.pmease.com/artifact?file=quickbuild-6.0.9.tar.gz&buildId=2820' -O quickbuild.tar && tar -zxvf quickbuild.tar -C /opt 
# Expose the default QB port
EXPOSE 8810
# start quickbuild
ENTRYPOINT /opt/quickbuild-6.0.9/bin/server.sh console
