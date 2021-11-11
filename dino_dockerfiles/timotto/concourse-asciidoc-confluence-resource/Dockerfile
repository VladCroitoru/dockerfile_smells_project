FROM maven

RUN \
  apt-get update \
  && apt-get install -y \
    jq \
    gettext

RUN \
  mvn dependency:get \
    -Dartifact=org.sahli.asciidoc.confluence.publisher:asciidoc-confluence-publisher-maven-plugin:0.3.0 \
  && mvn dependency:get \
    -Dartifact=org.codehaus.plexus:plexus-utils:1.1

ADD pom.template.xml /pom.template.xml

ADD assets /opt/resource
