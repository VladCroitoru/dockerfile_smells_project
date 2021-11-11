FROM jenkins/jenkins:lts

# Install useful plugins from file
# This kind of file can be created with "export-plugins-list.sh" script
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt

# Diable banner to install additionnal plugins
# https://github.com/jenkinsci/docker/blob/master/README.md
RUN echo 2.0 > /usr/share/jenkins/ref/jenkins.install.UpgradeWizard.state
