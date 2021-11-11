FROM python:2-slim

RUN mkdir -p /app/st2_exporter

WORKDIR /app/st2_exporter

COPY requirements.txt /app/st2_exporter
RUN pip install --no-cache-dir -r requirements.txt

COPY stackstorm_exporter.py /app/st2_exporter

EXPOSE 8000

ENTRYPOINT [ "python", "-u", "./stackstorm_exporter.py"]
