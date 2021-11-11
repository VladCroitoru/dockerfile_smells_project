FROM nginx:mainline
MAINTAINER Department of the Environment <devops@ris.environment.gov.au>

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python \
    python-jinja2

RUN rm /etc/nginx/conf.d/*
ADD html/ /usr/share/nginx/html/
ADD ssl/ /etc/nginx/ssl/

ADD scripts/ /scripts/

VOLUME ["/etc/nginx/ssl/", "/scripts/"]

EXPOSE 80 443

WORKDIR /scripts/
CMD ["python", "startup.py"]
