FROM scratch
MAINTAINER Dcylabs <dcylabs@gmail.com>
COPY ./dist/albatros-server /var/albatros/albatros-server 
COPY ./dist/ui /var/albatros/ui  
COPY ./dist/ca-certificates.crt /etc/ssl/certs/ca-certificates.crt
WORKDIR /var/albatros 
ENV DOCKER_ENDPOINT '/var/run/docker.sock'
ENV APP_PATH '/var/albatros/ui/build'
ENV SSL_KEY_PATH '/var/albatros/key.pem'
ENV SSL_CERT_PATH '/var/albatros/cert.pem'
ENV LISTEN_HTTP ':80'
ENV LISTEN_HTTPS ':443'
ENV USE_SSL '0'
ENV SESSION_TIME '600'
ENV SECRET 'thisisasecretreplaceit'
ENV ACCOUNTS 'username:$2a$10$PYzPqiPVrB8GIouPtSXA2eNYBxdkpc5NfOjMU6NoZdswMItdEJ6G6'
ENTRYPOINT ["/var/albatros/albatros-server"]