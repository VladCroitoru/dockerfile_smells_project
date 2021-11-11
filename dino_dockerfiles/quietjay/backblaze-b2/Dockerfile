FROM python:alpine3.7
RUN set -ex \
    && apk --update add git \
    && git clone https://github.com/Backblaze/B2_Command_Line_Tool.git \
    && cd B2_Command_Line_Tool \
    && python setup.py install
ENV B2_ACCOUNTID accountid
ENV B2_APPLICATIONKEY applicationkey
ADD entrypoint.sh /
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]