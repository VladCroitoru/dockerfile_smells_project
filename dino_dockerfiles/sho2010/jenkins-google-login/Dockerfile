FROM jenkinsci/jenkins:2.15

MAINTAINER Sho2010 "sho20100@gmail.com"

ENV GOOGLE_APP_CLIENT_ID = "YOUR_CLIENT_ID" \
    GOOGLE_APP_SECRET = "YOUR_SECRET"  \
    GOOGLE_ACCOUNT_DOMAIN = "google.com"

COPY google_login_plugins.txt /usr/share/jenkins/google_login_plugins.txt
COPY google_login.groovy /usr/share/jenkins/ref/init.groovy.d/google_login.groovy

RUN /usr/local/bin/plugins.sh /usr/share/jenkins/google_login_plugins.txt

ONBUILD COPY plugins.txt /usr/share/jenkins/plugins.txt
ONBUILD COPY custom.groovy /usr/share/jenkins/ref/init.groovy.d/custom.groovy

ONBUILD RUN /usr/local/bin/plugins.sh /usr/share/jenkins/plugins.txt

