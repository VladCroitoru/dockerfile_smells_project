FROM python:3.5-alpine

RUN apk add --update --no-cache git

WORKDIR /app
COPY requirements.frozen.txt /app
RUN pip install -r requirements.frozen.txt

COPY newversionchecker.py /app
CMD ["/app/newversionchecker.py"]
