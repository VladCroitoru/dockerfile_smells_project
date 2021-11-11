FROM alpine:3.3

RUN apk add --no-cache python3 && \
    apk add --no-cache --virtual=build-dependencies wget ca-certificates && \
    wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python3 && \
    apk del build-dependencies && \
    find / -name "__pycache__" -type d -exec rm -rf {} + && \
    ln -s /usr/bin/python3 /usr/local/bin/python

ENV PYTHONPATH /usr/src/app:$PYTHONPATH

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt && \
    find / -name "__pycache__" -type d -exec rm -rf {} +

COPY . /usr/src/app

CMD [ "./bin/stretchd.py" ]
