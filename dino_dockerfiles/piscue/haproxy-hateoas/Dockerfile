FROM haproxy:1.8.4-alpine
MAINTAINER Victor Sanahuja piscue@gmail.com
COPY haproxy-k8s.cfg /usr/local/etc/haproxy/haproxy.cfg
RUN adduser -D haproxy
RUN apk update && apk add openssl && \
    export CERT='/C=ES/ST=Barcelona/L=Barcelona/CN=test@example.com' && \
    openssl genrsa -out ca.key 4096 && \
    openssl req -new -x509 -days 365 -key ca.key -out ca.crt -subj "$CERT" && \
    openssl genrsa -out server.key 1024 && \
    openssl req -new -key server.key -out server.csr -subj "$CERT" && \
    openssl x509 -req -days 365 -in server.csr -CA ca.crt -CAkey ca.key \
    -set_serial 01 -out server.crt && \
    openssl genrsa -out client.key 1024 && \
    openssl req -new -key client.key -out client.csr -subj "$CERT" && \
    openssl x509 -req -days 365 -in client.csr -CA ca.crt -CAkey ca.key \
    -set_serial 02 -out client.crt && \
    cat server.crt server.key > server.pem && \
    mv server.pem /etc/ssl/private/example.com.pem
EXPOSE 443
CMD ["haproxy", "-f", "/usr/local/etc/haproxy/haproxy.cfg"]
#CMD ["sh"]
