FROM jenkins/jenkins

# Configure Jenkins
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
COPY init.groovy.d/* /usr/share/jenkins/ref/init.groovy.d/
