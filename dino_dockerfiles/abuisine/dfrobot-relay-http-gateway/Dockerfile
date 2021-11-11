FROM python:2.7-alpine
LABEL maintainer="Alexandre Buisine <alexandrejabuisine@gmail.com>" version="1.2"

COPY resources/gateway/ /usr/local/share/gateway/

RUN pip install web.py

EXPOSE 8080

WORKDIR /usr/local/share/gateway/

ENV RELAY_HOSTNAME= RELAY_PORT=2000

ENTRYPOINT ["python"]
CMD ["code.py"]