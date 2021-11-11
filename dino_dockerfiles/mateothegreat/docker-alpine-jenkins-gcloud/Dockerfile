#
# Derives from https://github.com/jenkinsci/docker/blob/master/Dockerfile-alpine
#
FROM jenkins/jenkins:2.128-alpine AS base

USER root

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENV GCLOUD_COMPONENTS="kubectl beta docker-credential-gcr"

VOLUME [ "/var/jenkins_home" ]

RUN apk add --update python docker make gettext nodejs py2-pip

RUN pip install awscli

RUN wget -O gradle.zip https://services.gradle.org/distributions/gradle-4.8-bin.zip && \
    unzip gradle.zip && rm -f gradle.zip && \
    ln -s /gradle-4.8/bin/gradle /usr/local/bin/gradle && \
    gradle --version

RUN wget https://dl.google.com/dl/cloudsdk/release/google-cloud-sdk.tar.gz && \
    tar zxvf google-cloud-sdk.tar.gz && \
    rm google-cloud-sdk.tar.gz && \
    ./google-cloud-sdk/install.sh --usage-reporting=true --path-update=true

# Add gcloud to the path
ENV PATH /google-cloud-sdk/bin:$PATH

# Configure gcloud for your project
RUN echo Yes | gcloud components install ${GCLOUD_COMPONENTS} 

COPY plugins.txt /usr/share/jenkins/ref/plugins.txt

RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

EXPOSE 8080 
EXPOSE 50001

CMD [ "./entrypoint.sh" ]