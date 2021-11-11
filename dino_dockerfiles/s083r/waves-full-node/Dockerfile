FROM alpine
ENV NETWORK_TYPE default
RUN apk add --no-cache curl && \
    LATEST_RELEASE=$(curl -L -s -H 'Accept: application/json' https://github.com/wavesplatform/Waves/releases/latest) && \
    LATEST_VERSION=$(echo $LATEST_RELEASE | sed -e 's/.*"tag_name":"\([^"]*\)".*/\1/') && \
    ARTIFACT_URL="https://github.com/wavesplatform/Waves/releases/download/$LATEST_VERSION/waves-all-"${LATEST_VERSION:1}".jar" && \
    curl -sLo /waves.jar "$ARTIFACT_URL"

FROM openjdk:9-jre-slim
COPY --from=0 /waves.jar /waves.jar
EXPOSE 6869 6868
CMD /usr/bin/java -jar /waves.jar /conf/${NETWORK_TYPE}.conf
