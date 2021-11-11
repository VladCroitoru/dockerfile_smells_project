FROM alpine:3.8

# JIRA Version that is installed
ENV JIRA_VERSION 8.4.0

RUN apk update && \
    apk add curl bash gzip ttf-dejavu

# Add glibc
RUN apk --no-cache add ca-certificates wget
RUN wget -q -O /etc/apk/keys/sgerrand.rsa.pub https://alpine-pkgs.sgerrand.com/sgerrand.rsa.pub
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.27-r0/glibc-2.27-r0.apk
RUN wget https://github.com/sgerrand/alpine-pkg-glibc/releases/download/2.27-r0/glibc-bin-2.27-r0.apk
RUN apk add glibc-2.27-r0.apk
RUN apk add glibc-bin-2.27-r0.apk

# Add the varfile
ADD response.varfile /response.varfile

# Install JIRA
RUN curl --progress-bar -L -O https://www.atlassian.com/software/jira/downloads/binary/atlassian-jira-software-${JIRA_VERSION}-x64.bin && \
    chmod a+x atlassian-jira-software-${JIRA_VERSION}-x64.bin && \
     ./atlassian-jira-software-${JIRA_VERSION}-x64.bin -q -varfile response.varfile && \
    rm -f /atlassian-jira-software-${JIRA_VERSION}-x64.bin && \
    adduser -D -H jira && \
    chown -R jira /opt/atlassian && \
    chown -R jira /var/atlassian

# Volume for JIRA data
VOLUME /var/atlassian/application-data/jira/

EXPOSE 8080

CMD ["/opt/atlassian/jira/bin/start-jira.sh", "-fg"]
