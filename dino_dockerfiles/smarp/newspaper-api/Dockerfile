FROM python:3.8-alpine

RUN apk add --update gcc git

# apk for Pillow
RUN apk add build-base py-pip jpeg-dev zlib-dev

# apkfor lxml
RUN apk add --virtual .build-deps \
        g++ \
        libxml2 \
        libxml2-dev && \
    apk add libxslt-dev && \
    apk del .build-deps

# apk for uwsgi
RUN apk add linux-headers

RUN pip install --no-cache-dir flask uwsgi html2text webpreview

#Clone newspaper project and checkout specific commit
RUN git clone https://github.com/codelucas/newspaper.git && \
    cd newspaper && git checkout 11cbf3a3038c0630d14e55743b942b6f36624a6b \
    && pip install -r requirements.txt

COPY . .
RUN python "/src/add_custom_certificates.py"

ENV NEWSPAPER_PORT 38765
EXPOSE $NEWSPAPER_PORT
CMD ["uwsgi", "--ini", "./src/wsgi.ini"]
