FROM debian:buster-slim
ARG TARGETPLATFORM
COPY .cache/${TARGETPLATFORM}/dd-wrt-wol-api /dd-wrt-wol-api
COPY .cache/${TARGETPLATFORM}/dd-wrt-wol-cli /dd-wrt-wol-cli
CMD [ "sh", "-exc", "exec /dd-wrt-wol-api $(echo \"$HOSTS_CONFIG\" | tr ';' '\n' | while read i; do echo \"-h$i\"; done)" ]
