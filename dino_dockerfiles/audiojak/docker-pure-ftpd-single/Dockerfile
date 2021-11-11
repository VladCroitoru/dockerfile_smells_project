FROM stilliard/pure-ftpd:hardened

MAINTAINER John Kennedy

ENV SINGLEUSER user
ENV SINGLEPASS password
RUN printf 'test123\ntest123\n' | pure-pw useradd $SINGLEUSER -u ftpuser -d /home/ftpusers/$SINGLEUSER
RUN pure-pw mkdb
