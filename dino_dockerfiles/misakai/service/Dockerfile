FROM misakai/mono:4.4.0
MAINTAINER Roman Atachiants "roman@misakai.com"

# Make sure we have S3 & additional libraries
RUN apt-get update -qq \
	&& apt-get install -y s3cmd libgdiplus libcurl3 libxml2 wget libc6 libc6-dev

# Application will be in app folder
WORKDIR /app
ADD . /app

# HTTP & HTTPS Ports
# EXPOSE 80
# EXPOSE 443

CMD ["/bin/bash", "/app/deploy.sh"]