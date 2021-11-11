FROM jboss/wildfly:10.1.0.Final
MAINTAINER Michael Schnell

ENV SWAGGER_VERSION 3.1.7
ENV SWAGGER_FILE swagger-ui-$SWAGGER_VERSION
ENV SWAGGER_TMP_DIR /var/tmp/$SWAGGER_FILE
ENV SWAGGER_API_URL http://petstore.swagger.io/v2/swagger.json

USER root

ADD $SWAGGER_FILE $SWAGGER_TMP_DIR
ADD prepare-env.sh $JBOSS_HOME/bin
RUN chown -R jboss:jboss $JBOSS_HOME/bin/prepare-env.sh &&\
    chmod +x $JBOSS_HOME/bin/prepare-env.sh

CMD ["/opt/jboss/wildfly/bin/prepare-env.sh", "/opt/jboss/wildfly/bin/standalone.sh", "-b", "0.0.0.0"]
