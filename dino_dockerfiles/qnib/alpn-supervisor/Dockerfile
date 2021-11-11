FROM qnib/alpn-base

RUN apk add --update py-pip \
 && pip install --upgrade pip \
 && pip install supervisor \
 && mkdir -p /var/log/supervisor/ \
 && rm -rf /var/cache/apk/*
ADD etc/supervisord.conf /etc/
ADD opt/qnib/supervisor/bin/start.sh /opt/qnib/supervisor/bin/
CMD [ "/opt/qnib/supervisor/bin/start.sh", "-n" ]
RUN echo "/opt/qnib/supervisor/bin/start.sh" >> /root/.bash_history \
 && echo "supervisorctl status" >> /root/.bash_history
