FROM jetty

EXPOSE 8443

COPY tweak-ssl.xml $JETTY_HOME/etc/

RUN java -jar $JETTY_HOME/start.jar -Djdk.tls.rejectClientInitiatedRenegotiation=true --add-to-startd=http2 --approve-all-licenses

CMD ["java","-Djava.io.tmpdir=/tmp/jetty","-Djdk.tls.rejectClientInitiatedRenegotiation=true","-Djdk.tls.ephemeralDHKeySize=2048","-jar","/usr/local/jetty/start.jar"]
