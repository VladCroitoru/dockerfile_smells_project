FROM python:latest
MAINTAINER Michael Halstead <mhalstead@linuxfoundation.org>

ENV PYTHONUNBUFFERED 1
ENV CROPS_WEBHOOK_KEY None
ENV CROPS_WEBHOOK_CONFIG /etc/crops-webhook/crops_webhook.cfg

RUN pip install gunicorn
RUN git clone https://github.com/crops/webhook.git /root/webhook
RUN cd /root/webhook && python setup.py install
RUN mkdir -p /etc/crops-webhook
ADD crops_webhook.cfg /etc/crops-webhook/crops_webhook.cfg
RUN git clone https://github.com/crops/webhook-handlers.git /etc/crops-webhook/handlers

ADD update_handlers.sh /etc/crops-webhook/handlers/
ADD crops_app.py /opt/webhook/

RUN mkdir /opt/workdir
RUN adduser --system webhook
RUN chown -R webhook /opt /etc/crops-webhook
RUN chown root:root /etc/crops-webhook/handlers/update_handlers.sh && chmod 555 /etc/crops-webhook/handlers/update_handlers.sh
ADD whitelist /etc/crops-webhook/whitelist

USER webhook
CMD ["/usr/local/bin/gunicorn", "crops_app:app", "--workers=4", "--bind=:5000", "--log-level=debug", "--chdir=/opt/webhook"]
