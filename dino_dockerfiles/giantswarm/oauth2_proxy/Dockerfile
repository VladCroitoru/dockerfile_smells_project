FROM alpine:3.7

RUN mkdir -p /opt/oauth2_proxy
ADD ./oauth2_proxy /opt/oauth2_proxy/oauth2_proxy

# Install CA certificates
RUN apk add --no-cache --virtual=build-dependencies ca-certificates

WORKDIR /opt/oauth2_proxy

# Expose the ports we need and setup the ENTRYPOINT w/ the default argument
EXPOSE 8080 4180
ENTRYPOINT ["/opt/oauth2_proxy/oauth2_proxy"]
CMD ["--upstream=http://0.0.0.0:8080/", "--http-address=0.0.0.0:4180"]
