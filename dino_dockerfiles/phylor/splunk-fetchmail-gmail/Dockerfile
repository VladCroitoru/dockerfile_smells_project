FROM splunk/splunk

ENV SPLUNK_START_ARGS "--accept-license --answer-yes --no-prompt"

RUN apt update && apt install -y fetchmail procmail

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
COPY fetch_mails.sh /
RUN chmod +x /fetch_mails.sh
RUN mkdir -p /home/splunk/Mail && chown splunk:splunk /home/splunk/Mail
RUN touch /var/log/fetchmail.log && chown splunk:splunk /var/log/fetchmail.log

COPY inputs.conf /opt/splunk/etc/system/local/
COPY props.conf /opt/splunk/etc/system/local/
COPY transforms.conf /opt/splunk/etc/system/local/

COPY inputs.conf /
COPY props.conf /
COPY transforms.conf /

CMD /entrypoint.sh

