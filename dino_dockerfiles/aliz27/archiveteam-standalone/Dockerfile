FROM ubuntu
MAINTAINER Daniel Ahlberg <aliz@tamperd.net>
RUN apt-get update && apt-get install -y git libgnutls-dev lua5.1 liblua5.1-0 liblua5.1-0-dev python-dev python-pip bzip2 zlib1g-dev build-essential automake curl flex unzip && rm -rf /var/lib/apt/lists/*
RUN pip install --upgrade seesaw requests warc --no-cache-dir
RUN curl -o /tmp/wget-lua.tar.bz2 https://warriorhq.archiveteam.org/downloads/wget-lua/wget-1.14.lua.20160530-955376b.tar.bz2 \
	&& cd /tmp && tar -jxvf wget-lua.tar.bz2 && cd /tmp/wget-1.14.lua*; ./configure; make && cp ./src/wget /usr/bin/wget-lua && rm -fr /tmp/wget*
RUN curl -L -o /tmp/wpull.zip https://launchpad.net/wpull/trunk/v2.0.1/+download/wpull-2.0.1-linux-x86_64-3.4.3-20161230193838.zip \
	&& cd /tmp && unzip wpull.zip && mv wpull /usr/bin && rm -fr /tmp/wpull*
COPY doatjob.sh doatjob.sh
ENTRYPOINT ["./doatjob.sh"]

