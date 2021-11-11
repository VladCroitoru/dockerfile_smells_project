FROM robertbrem/payara

MAINTAINER Robert Brem <brem_robert@hotmail.com>

RUN echo ${DOMAIN_NAME}
RUN ./asadmin start-domain ${DOMAIN_NAME} && \
    ./asadmin delete-jvm-options -Xmx512m  && \
    ./asadmin create-jvm-options -Xms750m  && \
    ./asadmin create-jvm-options -Xmx750m  && \
    ./asadmin stop-domain ${DOMAIN_NAME}
