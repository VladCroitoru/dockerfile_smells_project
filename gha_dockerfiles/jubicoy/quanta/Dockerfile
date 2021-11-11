FROM adoptopenjdk/maven-openjdk11 AS builder

RUN apt-get update && apt-get install ca-certificates -y

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
  && apt-get install -y nodejs git \
  && mkdir -p /opt/build/front /opt/build/lib

COPY pom.xml /opt/build/
RUN cd /opt/build \
  && mvn dependency:copy-dependencies dependency:resolve dependency:resolve-plugins dependency:go-offline -B

COPY front/package.json /opt/build/front/
COPY front/package-lock.json /opt/build/front/
RUN cd /opt/build/front \
  && npm ci

COPY ./ /opt/build/

RUN cd /opt/build \
  # Read project.artifactId and project.version from pom.xml into a variable
  && export ARTIFACT=$(mvn -q -Dexec.executable=echo -Dexec.args='${project.artifactId}-${project.version}' --non-recursive exec:exec) \
  # Package with shade profile so all libraries are included
  && mvn clean package -P shade \
  && mv target/${ARTIFACT}.jar /opt/${ARTIFACT}.jar \
  && cd /opt \
  && rm -rf /opt/build \
  && chmod a+x /opt/${ARTIFACT}.jar \
  && echo "${ARTIFACT}.jar" > /opt/artifact

FROM adoptopenjdk/openjdk11:debian-jre

RUN mkdir -p /opt
COPY --from=0 /opt/*.jar /opt/
COPY --from=0 /opt/artifact /opt/

EXPOSE 8080

CMD java -jar /opt/$(cat /opt/artifact)
