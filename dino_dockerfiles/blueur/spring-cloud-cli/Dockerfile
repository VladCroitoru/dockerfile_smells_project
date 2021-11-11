FROM openjdk:latest

MAINTAINER blueur

ARG SPRING_BOOT_VERSION
ENV SPRING_BOOT_VERSION ${SPRING_BOOT_VERSION:-1.5.2.RELEASE}
ARG SPRING_CLOUD_VERSION
ENV SPRING_CLOUD_VERSION ${SPRING_CLOUD_VERSION:-1.2.3.RELEASE}

RUN wget -O spring-boot-cli.tar.gz http://repo.spring.io/release/org/springframework/boot/spring-boot-cli/${SPRING_BOOT_VERSION}/spring-boot-cli-${SPRING_BOOT_VERSION}-bin.tar.gz \
 && tar -zxf spring-boot-cli.tar.gz --strip-components=1 \
 && rm spring-boot-cli.tar.gz

RUN spring install org.springframework.cloud:spring-cloud-cli:${SPRING_CLOUD_VERSION}

ENTRYPOINT ["spring"]
