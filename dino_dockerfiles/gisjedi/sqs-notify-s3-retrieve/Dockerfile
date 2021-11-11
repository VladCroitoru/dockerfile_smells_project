FROM python:2-alpine

RUN mkdir /app && mkdir /incoming && ln -s /incoming /app/incoming
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && \
    echo Patch boto3 buffer_size to increase download performance && \
    sed -i 's/\*\ 16/\*\ 256/g' /usr/local/lib/python2.7/site-packages/boto3/s3/transfer.py

COPY . /app/

# Volume where S3 data will arrive by default
VOLUME /incoming

ENTRYPOINT ["python", "s3_retrieve.py"]
CMD ["-h"]