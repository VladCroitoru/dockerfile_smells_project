     # ###### #    # #    # # #    #  ####      ####  #####  ####  #####  #    # Ephemeral
     # #      ##   # #   #  # ##   # #         #        #   #    # #    # ##  ## Template
     # #####  # #  # ####   # # #  #  ####      ####    #   #    # #    # # ## # v0.0.6
     # #      #  # # #  #   # #  # #      #         #   #   #    # #####  #    #
#    # #      #   ## #   #  # #   ## #    #    #    #   #   #    # #   #  #    #
 ####  ###### #    # #    # # #    #  ####      ####    #    ####  #    # #    # MIT Licensed

FROM jenkins/jenkins:latest
COPY plugins.txt /usr/share/jenkins/ref/plugins.txt
RUN /usr/local/bin/install-plugins.sh < /usr/share/jenkins/ref/plugins.txt
COPY initialConfig.groovy /usr/share/jenkins/ref/init.groovy.d/initialConfigs.groovy
COPY jenkins.yml /usr/share/jenkins/ref/jenkins.yml
ENV JAVA_OPTS -Djenkins.install.runSetupWizard=false
