FROM java:8-alpine
RUN apk --update add tar tmux supervisor procps jq unzip gnupg curl nss nginx

# NEM software
RUN curl -L http://bob.nem.ninja/nis-0.6.95.tgz > nis-0.6.95.tgz
RUN tar zxf nis-0.6.95.tgz

# servant
RUN curl -L https://github.com/rb2nem/nem-servant/raw/master/servant.zip > servant.zip
RUN unzip servant.zip

# config
RUN rm -f /package/nis/config.properties
RUN ln -snf /etc/nis-config/config.properties /package/nis/config.properties

# Tuning supervisor
RUN sed -i 's/^\(\[supervisord\]\)$/\1\nnodaemon=true/' /etc/supervisord.conf

# Copy supervisor conf
RUN mkdir /etc/supervisor.d/
COPY programs.ini /etc/supervisor.d/programs.ini

ADD nginx.conf /etc/nginx/nginx.conf

EXPOSE 7890

VOLUME /root
VOLUME /etc/nis-ssl
VOLUME /etc/nis-config

CMD ["/usr/bin/supervisord"]
