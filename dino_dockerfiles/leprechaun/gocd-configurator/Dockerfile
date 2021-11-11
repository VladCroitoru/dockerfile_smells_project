FROM python:2-alpine

ADD requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD gocd_configurator.py /usr/local/bin/gocd_configurator
RUN chmod 755 /usr/local/bin/gocd_configurator

WORKDIR /tmp

CMD ["python", "/usr/local/bin/gocd_configurator", "gocd-config.yml"]
