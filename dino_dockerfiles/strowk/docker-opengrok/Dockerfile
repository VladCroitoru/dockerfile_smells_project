FROM tomcat:9
ENV OPENGROK_RELEASE 1.1-rc17
RUN wget "https://github.com/OpenGrok/OpenGrok/releases/download/${OPENGROK_RELEASE}/opengrok-${OPENGROK_RELEASE}.tar.gz" -O /tmp/oopengrok-${OPENGROK_RELEASE}.tar.gz
RUN apt-get update
RUN apt-get install -y git && git clone https://github.com/universal-ctags/ctags
RUN apt-get install -y autoconf
RUN apt-get install -y pkg-config
RUN apt-get install -y automake
RUN apt-get install -y make
RUN apt-get install -y gcc
RUN apt-get install -y procps

RUN cd ctags && ./autogen.sh && ./configure  && make && make install
RUN tar zxvf /tmp/oopengrok-${OPENGROK_RELEASE}.tar.gz -C /


ENV SRC_ROOT /src
ENV OPENGROK_TOMCAT_BASE /usr/local/tomcat
ENV CATALINA_HOME /usr/local/tomcat
ENV PATH $CATALINA_HOME/bin:$PATH
ENV PATH /opengrok-${OPENGROK_RELEASE}/bin:$PATH

ENV CATALINA_BASE /usr/local/tomcat
ENV CATALINA_HOME /usr/local/tomcat
ENV CATALINA_TMPDIR /usr/local/tomcat/temp
ENV JRE_HOME /usr
ENV CLASSPATH /usr/local/tomcat/bin/bootstrap.jar:/usr/local/tomcat/bin/tomcat-juli.jar

WORKDIR $CATALINA_HOME
RUN /opengrok-${OPENGROK_RELEASE}/bin/OpenGrok deploy
EXPOSE 8080

ADD scripts/internal/ /scripts
RUN find /scripts | grep -E '\.sh$' | xargs -r chmod +x
RUN mkdir /src
RUN mkdir /data
RUN mkdir /config
ENV OPENGROK_READ_XML_CONFIGURATION /config/custom.xml

ENV PATH /scripts:$PATH
CMD ["/scripts/start.sh"]



