FROM  python:3.6.4-alpine3.7

RUN apk add --update \
	&& apk --no-cache add git \
	&& rm -rf /var/cache/apk/*

RUN mkdir /app

WORKDIR /app

RUN git clone https://github.com/jeremy886/GreatQuotes.git

WORKDIR /app/GreatQuotes

RUN pip install -r requirements.txt

EXPOSE 8080

CMD ["python", "webapp.py"]
