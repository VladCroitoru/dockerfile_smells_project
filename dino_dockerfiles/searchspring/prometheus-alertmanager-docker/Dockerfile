FROM prom/alertmanager

COPY alertmanager/* /etc/alertmanager/

CMD [ '-config.file=/etc/alertmanager/config.yml', '-storage.path=/alertmanager']