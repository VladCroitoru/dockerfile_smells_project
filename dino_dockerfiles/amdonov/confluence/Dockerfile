FROM alpine:3.4
ENV JAVA_HOME=/usr
RUN apk --update add curl bash openjdk8-jre && rm -rf /var/cache/apk/*
RUN curl -k -o confluence.tgz https://downloads.atlassian.com/software/confluence/downloads/atlassian-confluence-5.10.0.tar.gz && \
    tar xfz confluence.tgz && \
    rm confluence.tgz && \
    mkdir -p /opt/atlassian && mv atlassian* /opt/atlassian/confluence && \
    echo "confluence.home=/var/atlassian/application-data/confluence" > /opt/atlassian/confluence/confluence/WEB-INF/classes/confluence-init.properties && \
    mkdir -p /var/atlassian/application-data/confluence
# Allow confluence to run as any user for OpenShift
RUN chmod -R 777 /opt/atlassian/confluence/logs /opt/atlassian/confluence/work /opt/atlassian/confluence/temp /opt/atlassian/confluence/conf /var/atlassian/application-data/confluence
EXPOSE 8090
VOLUME /var/atlassian/application-data/confluence
CMD /opt/atlassian/confluence/bin/start-confluence.sh -fg
