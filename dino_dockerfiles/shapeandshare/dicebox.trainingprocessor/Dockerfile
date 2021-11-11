FROM python:2.7

WORKDIR /app

COPY ./app /app
COPY ./dicebox/dicebox /app/dicebox
COPY ./dicebox/dicebox.config /app

RUN pip install -r requirements.txt \
    && useradd -M -U -u 1000 trainingprocessor \
    && chown -R trainingprocessor /app

ENTRYPOINT ["python", "./trainingprocessor.py"]
#CMD ["su", "-", "trainingprocessor", "-c", "tail", "-f", "./logs/trainingprocessor.log"]
