FROM certbot/certbot

RUN pip install certbot-dns-cloudxns

COPY entrypoint.sh entrypoint.sh

ENTRYPOINT [ "./entrypoint.sh" ]
