FROM mysql:5.6

ENV GOF3R_VERSION=0.4.10 AWS_ACCESS_KEY_ID=none AWS_SECRET_ACCESS_KEY=none S3_BUCKET="none" S3_OBJ="test.sql" 


# Install supervisor and s3gof3r
RUN apt-get update && \
	apt-get -y install wget ca-certificates lsof pv && \
	wget https://github.com/rlmcpherson/s3gof3r/releases/download/v0.4.10/gof3r_${GOF3R_VERSION}_linux_amd64.tar.gz \
		-O gof3r.tar.gz --no-check-certificate && \
	tar xvfz gof3r.tar.gz && \
	cd gof3r_${GOF3R_VERSION}_linux_amd64 && \
	echo "log-error /dev/stderr > /etc/mysql/conf.d/logerror" && \
	cp gof3r /usr/local/bin

COPY docker-entrypoint.sh /entrypoint.sh
COPY my-mini.cnf /my-mini.cnf

RUN chmod 755 /*.sh

# TODO: Do something to reduce the MySQL footprint, or get bigger machines