FROM quay.io/ukhomeofficedigital/alpine:v3.14 as builder

USER root

RUN apk add --no-cache openjdk11-jre

COPY build/libs/*.jar .

RUN java -Djarmode=layertools -jar *.jar extract

FROM quay.io/ukhomeofficedigital/alpine:v3.14

USER root

RUN apk add --no-cache openjdk11-jre

WORKDIR /app

ENV USER user_hocs
ENV USER_ID 1000
ENV GROUP group_hocs

RUN addgroup -S ${GROUP} && \
    adduser -S -u ${USER_ID} ${USER} -G ${GROUP} -h /app && \
    mkdir -p /app && \
    chown -R ${USER}:${GROUP} /app

COPY scripts/run.sh /app/scripts/run.sh

RUN chmod a+x /app/scripts/*

COPY --from=builder dependencies/ ./
COPY --from=builder snapshot-dependencies/ ./
RUN true # Bug where copying with 0 action then copying again throws an error
COPY --from=builder spring-boot-loader/ ./
COPY --from=builder application/ ./

EXPOSE 8080

USER ${USER_ID}

CMD ["sh", "/app/scripts/run.sh"]
