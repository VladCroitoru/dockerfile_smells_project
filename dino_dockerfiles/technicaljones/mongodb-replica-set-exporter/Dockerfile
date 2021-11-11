FROM python:3-slim

EXPOSE 8000

WORKDIR /app/mongodb_exporter

ADD requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

ADD exporter/exporter.py .

ENTRYPOINT [ "python", "-u", "./exporter.py" ]

