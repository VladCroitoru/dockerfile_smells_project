FROM python:3.6.9-alpine3.10

EXPOSE 8000
RUN apk add --no-cache curl
ADD scripts/start.sh /
RUN chmod +x /start.sh
ADD requirements.txt /tmp
RUN pip install --no-cache-dir -r /tmp/requirements.txt
RUN  rm /tmp/requirements.txt
WORKDIR /app
COPY src .

CMD [ "/start.sh" ]
