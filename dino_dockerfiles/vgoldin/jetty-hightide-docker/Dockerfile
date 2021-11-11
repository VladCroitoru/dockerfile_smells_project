FROM java

MAINTAINER vgoldin@gmail.com

# Install Jetty
RUN wget http://dist.codehaus.org/jetty/jetty-hightide-7.5.1/jetty-hightide-7.5.1.v20110908.tar.gz -O /tmp/jetty.tar.gz
		 
# Unpack
RUN tar -xvzf /tmp/jetty.tar.gz -C /opt
RUN mv /opt/jetty-hightide-7.5.1.v20110908 /opt/jetty
RUN rm /tmp/jetty.tar.gz
RUN rm -rf /opt/jetty/webapps/*
RUN rm -rf /opt/jetty/contexts

ENV JETTY_HOME /opt/jetty
ENV PATH $PATH:$JETTY_HOME/bin

CMD /opt/jetty/bin/deploy-and-run.sh
