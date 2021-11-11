FROM python:2.7

WORKDIR /app

COPY ./app /app
COPY ./dicebox/dicebox /app/dicebox
COPY ./dicebox/dicebox.config /app

RUN pip install -r requirements.txt \
    && useradd -M -U -u 1000 batchprocessor \
    && chown -R batchprocessor /app

ENTRYPOINT ["python", "./sensory_service_batch_processor.py"]
