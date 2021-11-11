FROM python:alpine3.6

RUN pip install --no-cache-dir prometheus_client requests
ADD spring_boot_exporter.py /spring_boot_exporter.py
RUN chmod +x /spring_boot_exporter.py

ENTRYPOINT ["/spring_boot_exporter.py"]