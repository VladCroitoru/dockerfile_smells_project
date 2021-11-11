FROM scratch

ENV RESOLVER_HOST 0.0.0.0
ENV RESOLVER_PORT 4000
ENV RESOLVER_STORE /data/datastore.json
ENV RESOLVER_USER admin
ENV RESOLVER_KEY $apr1$rZTtRFsq$BK1GqipOMOTpWuJYuDtJ01

VOLUME ["/data"]

# Add binary
ADD ./bin/resolver resolver

# To make SSL requests, we need the SSL Root certificates. We need to add
# them to the container because they aren't present.
ADD ca-certificates.crt /etc/ssl/certs/

EXPOSE $RESOLVER_PORT

ENTRYPOINT ["/resolver"]
