FROM odoo:10.0
MAINTAINER tedi3231
USER root
RUN apt-get update
RUN apt-get install -y --no-install-recommends build-essential libssl-dev libffi-dev python-dev
RUN set -x; \
	    pip install -U setuptools \
	 &&	pip install cryptography \
	 && pip install wechatpy \
  	 && pip install redis \
	 && pip install pika

RUN chown -R odoo:odoo /var/lib/odoo
#USER odoo
