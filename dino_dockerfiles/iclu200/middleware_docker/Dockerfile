FROM centos

MAINTAINER iclu200(iclu200@gmail.com)

RUN yum update -y && \
    yum install -y java-1.8.0 \
    wget \
    unzip && \
    yum clean all

RUN mkdir -p /middleware && \
    cd /middleware && \
    wget https://s3-ap-northeast-1.amazonaws.com/itrimiddleware/middleware_20160129.zip && \
    unzip ./middleware_20160129.zip && \
    rm middleware_20160129.zip

EXPOSE 8511 8512 8513 8514 8515 8516

CMD RMI_HOST=`wget -q -O - http://169.254.169.254/latest/meta-data/public-hostname` && cd /middleware && java -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.port=8514 -Dcom.sun.management.jmxremote.local.only=false -Dcom.sun.management.jmxremote.authenticate=false -Dcom.sun.management.jmxremote.ssl=false -Djava.rmi.server.hostname=$RMI_HOST -Dcom.sun.management.jmxremote.rmi.port=8514 -cp SocketServerConsole.jar fy103.Main ./config.xml
#for testing
