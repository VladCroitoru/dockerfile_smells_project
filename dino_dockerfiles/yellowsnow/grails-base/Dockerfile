FROM dockeruser/oracle-java7-jdk

WORKDIR /opt/grails

ADD grails /opt/grails

RUN ./grailsw refresh-dependencies

ENTRYPOINT ["/bin/bash", "/opt/grails/grailsw"]
CMD ["-version"]
