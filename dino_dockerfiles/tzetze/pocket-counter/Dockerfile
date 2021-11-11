FROM alpine:3.1

RUN apk add --update python py-pip
RUN apk -U upgrade && \
    apk -U add python ca-certificates && \
    update-ca-certificates

COPY requirements.txt /
RUN pip install -r requirements.txt
COPY src /

expose 4242
CMD ["python", "app.py"]
