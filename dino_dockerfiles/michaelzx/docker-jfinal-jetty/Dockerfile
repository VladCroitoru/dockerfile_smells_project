FROM martinseeler/oracle-server-jre:latest

ENV JETTY_HOME /usr/local/jetty
ENV PATH $JETTY_HOME/bin:$PATH
RUN mkdir -p "$JETTY_HOME"
WORKDIR $JETTY_HOME

ENV TZ Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
ENV LANG C.UTF-8
ENV JETTY_VERSION 8.1.17.v20150415
ENV JETTY_TGZ_URL http://central.maven.org/maven2/org/eclipse/jetty/jetty-distribution/$JETTY_VERSION/jetty-distribution-$JETTY_VERSION.tar.gz
RUN echo $JETTY_TGZ_URL

RUN apk --update add curl tar bash\
	&& curl -SL "$JETTY_TGZ_URL" -o jetty.tar.gz \
    && tar -xvf jetty.tar.gz --strip-components=1 \
    && sed -i '/jetty-logging/d' etc/jetty.conf \
    && rm -fr javadoc \
    && rm jetty.tar.gz* \
    && rm contexts/javadoc.xml \
    && rm contexts/test.xml \
    && rm -fr contexts/test.d \
    && rm webapps/spdy.war \
    && rm webapps/test.war \
    && apk del curl tar

EXPOSE 8080
CMD ["jetty.sh", "run"]