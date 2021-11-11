FROM python

ENV S3_PAGE_SIZE 1000
ENV S3_OBJECT_AGE 365

RUN pip install boto3 pytz
RUN mkdir /app

COPY cleanup.py /app/cleanup.py

ENTRYPOINT ["/app/cleanup.py"]
