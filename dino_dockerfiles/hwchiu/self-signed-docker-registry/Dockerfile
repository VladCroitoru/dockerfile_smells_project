FROM registry:2

COPY entrypoint.sh /
COPY req.cnf /

RUN apk add --no-cache openssl

ENV OUTPUT=domain.crt
ENV KEY_OUTPUT=domain.key
ENV CN=192.168.1.1

EXPOSE 443

ENTRYPOINT ["/entrypoint.sh"]
CMD ["serve", "/etc/docker/registry/config.yml"]
