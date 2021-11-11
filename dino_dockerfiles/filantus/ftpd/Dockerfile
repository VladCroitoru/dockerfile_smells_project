FROM python:3.6-slim-stretch

RUN pip install pyftpdlib
RUN mkdir /var/ftp

COPY ./ftpd.py /srv/

CMD python /srv/ftpd.py
