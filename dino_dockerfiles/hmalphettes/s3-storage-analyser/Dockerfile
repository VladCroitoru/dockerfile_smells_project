FROM python:3-slim

COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt

COPY *.py /app/

WORKDIR /app
USER nobody
ENTRYPOINT [ "python3", "-m" ]

CMD [ "s3_storage_analyser" ]
