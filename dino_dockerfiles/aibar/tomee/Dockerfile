FROM aibar/jvm:1.8

EXPOSE 8080

ENTRYPOINT ["/tomee/bin/catalina.sh", "run"]

RUN wget http://apache.hippo.nl/tomee/tomee-1.7.4/apache-tomee-1.7.4-plus.tar.gz \
         -O tomee.tar.gz && \
    
    tar xf tomee.tar.gz && rm tomee.tar.gz && \
    mv apache-tomee-plus-1.7.4 tomee && \
    rm -rf tomee/webapps/* && \
    
    wget http://repo1.maven.org/maven2/org/eclipse/persistence/eclipselink/2.6.4/eclipselink-2.6.4.jar \
         -O tomee/lib/eclipselink.jar && \

    ln -s /tomee/webapps /webapps && \
    ln -s /tomee/apps /apps

COPY tomee.xml /tomee/conf/

VOLUME ["/webapps", "/apps"]