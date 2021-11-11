FROM sonarqube:5.4
MAINTAINER Ernesto Hernandez "ehdez73@gmail.com"

EXPOSE 9000

ENV SERVICE_NAME="sonar"
ENV PLUGIN_FOLDER="/opt/sonarqube/extensions/plugins"

# Add language plugins
ADD https://sonarsource.bintray.com/Distribution/sonar-java-plugin/sonar-java-plugin-3.12.jar $PLUGIN_FOLDER
ADD http://downloads.sonarsource.com/plugins/org/codehaus/sonar-plugins/python/sonar-python-plugin/1.5/sonar-python-plugin-1.5.jar $PLUGIN_FOLDER
ADD https://sonarsource.bintray.com/Distribution/sonar-javascript-plugin/sonar-javascript-plugin-2.11.jar $PLUGIN_FOLDER
ADD https://sonarsource.bintray.com/Distribution/sonar-groovy-plugin/sonar-groovy-plugin-1.3.1.jar $PLUGIN_FOLDER
ADD http://sonarsource.bintray.com/Distribution/sonar-php-plugin/sonar-php-plugin-2.8.jar $PLUGIN_FOLDER
ADD https://github.com/ehdez73/sonar-scala-plugin/releases/download/0.3.0-SNAPSHOT/sonar-scala-plugin-0.3.0-SNAPSHOT.jar $PLUGIN_FOLDER

# Add other plugins
ADD https://github.com/SonarQubeCommunity/sonar-build-breaker/releases/download/2.0/sonar-build-breaker-plugin-2.0.jar $PLUGIN_FOLDER
ADD https://sonarsource.bintray.com/Distribution/sonar-github-plugin/sonar-github-plugin-1.1.jar $PLUGIN_FOLDER