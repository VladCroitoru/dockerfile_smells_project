FROM jenkins/jenkins:lts
ENV JAVA_OPTS="-Dhudson.Main.development=true -Djenkins.install.runSetupWizard=false"
COPY executors.groovy /usr/share/jenkins/ref/init.groovy.d/executors.groovy
COPY set-hostname.groovy /usr/share/jenkins/ref/init.groovy.d/set-hostname.groovy
COPY cas.groovy /usr/share/jenkins/ref/init.groovy.d/cas.groovy
RUN /usr/local/bin/install-plugins.sh ldap thinBackup hipchat cas-plugin matrix-auth
