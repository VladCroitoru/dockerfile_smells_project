FROM openjdk:8

# JCE Setup

RUN cd /tmp/ && \
    curl -LO "http://download.oracle.com/otn-pub/java/jce/8/jce_policy-8.zip" -H 'Cookie: oraclelicense=accept-securebackup-cookie' && \
    unzip jce_policy-8.zip && \
    rm jce_policy-8.zip && \
    yes |cp -v /tmp/UnlimitedJCEPolicyJDK8/*.jar /docker-java-home/jre/lib/security

# Run Annoying34 Backend

COPY gradle gradle
COPY build.gradle .
COPY gradlew .
COPY src src

RUN ./gradlew build

EXPOSE 8080

CMD ["java", "-jar", "build/libs/annoying34-backend-0.1.0.jar"]