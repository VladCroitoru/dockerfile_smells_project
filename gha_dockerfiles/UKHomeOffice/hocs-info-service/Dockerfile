FROM quay.io/ukhomeofficedigital/alpine:v3.13

ENV USER user_hocs_info_service
ENV USER_ID 1000
ENV GROUP group_hocs_info_service
ENV NAME hocs-info-service
ENV JAR_PATH build/libs

USER root

RUN apk add openjdk11-jre

WORKDIR /app

RUN addgroup -S ${GROUP} && \
    adduser -S -u ${USER_ID} ${USER} -G ${GROUP} -h /app && \
    mkdir -p /app && \
    chown -R ${USER}:${GROUP} /app

COPY ${JAR_PATH}/${NAME}*.jar /app

ADD scripts /app/scripts

RUN chmod a+x /app/scripts/*

EXPOSE 8080

USER ${USER_ID}

CMD ["sh", "/app/scripts/run.sh"]