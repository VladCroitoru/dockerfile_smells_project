FROM  alpine
LABEL MAINTAINER "Lisle Mose <lmose@email.unc.edu>"
LABEL MAINTAINER "Alan Hoyle <alanh@unc.edu>"

RUN apk -U add \
     libc6-compat \ 
     openjdk8

ARG ABRA2_VERSION=2.24
ENV ABRA2_VERSION ${ABRA2_VERSION}
ENV JAVA_OPTS "-Xmx16G"

RUN mkdir /opt/abra/
ADD https://github.com/mozack/abra2/releases/download/v${ABRA2_VERSION}/abra2-${ABRA2_VERSION}.jar /opt/abra/

RUN chmod 755 /opt/abra/abra2-${ABRA2_VERSION}.jar && \
    ln -s /opt/abra/abra2-${ABRA2_VERSION}.jar /opt/abra/abra2.jar 

# ENTRYPOINT [ "java", "-jar", "/abra2.jar" ]
# CMD [ --help ]
