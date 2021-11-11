FROM maven:latest

RUN apt-get update && \
    apt-get install \
                    vim \
                    apt-transport-https \
                    netcat \
                    socat \
                    net-tools \
                    vifm \
                    tcpdump \
                    file \
                    xmlstarlet \
                    jq \
                    zip \
                    hexedit -y --no-install-recommends \
    && mkdir /opt/gradle && wget https://services.gradle.org/distributions/gradle-4.3.1-bin.zip -O /tmp/gradle.zip \
    && unzip /tmp/gradle.zip -d /opt/gradle/ && rm -f /tmp/gradle.zip \
    && wget https://repo.spring.io/release/org/springframework/boot/spring-boot-cli/1.5.9.RELEASE/spring-boot-cli-1.5.9.RELEASE-bin.tar.gz -O /tmp/spring-boot-cli.tar.gz \
    && tar -xf /tmp/spring-boot-cli.tar.gz -C /opt/ && rm -f /tmp/spring-boot-cli.tar.gz \
    && wget https://github.com/JetBrains/kotlin/releases/download/v1.2.10/kotlin-compiler-1.2.10.zip -O /tmp/kotlin.zip && unzip /tmp/kotlin.zip -d /opt/ && rm -f /tmp/kotlin.zip \
    && echo "export PATH=/opt/gradle/gradle-4.3.1/bin:/opt/spring-1.5.9.RELEASE/bin:/opt/kotlinc/bin:$PATH" >> /root/.bashrc
