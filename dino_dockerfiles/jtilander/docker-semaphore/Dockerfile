FROM jtilander/ansible
MAINTAINER Jim Tilander

ENV SEMAPHORE_VERSION=2.3.0 SEMAPHORE_PLATFORM=amd64

RUN apk add --no-cache git curl openssh

RUN curl -SsL "https://github.com/ansible-semaphore/semaphore/releases/download/v${SEMAPHORE_VERSION}/semaphore_linux_${SEMAPHORE_PLATFORM}" > /usr/bin/semaphore && \
	chmod a+x /usr/bin/semaphore

RUN mkdir -p /data /app

WORKDIR /app

EXPOSE 3000

ENV MYSQL_ADDR=mysql
ENV ADMIN_USER=admin
ENV ADMIN_PASSWORD=password
ENV ADMIN_EMAIL=admin@localhost
ENV MY_URL=http://semaphore:8080/

COPY Readme.md /
COPY docker-entrypoint.sh /

CMD ["semaphore"]
