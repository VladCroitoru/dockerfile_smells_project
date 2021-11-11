FROM python:3.4-alpine
RUN mkdir -p /usr/src/app
COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY dns-zone-from-yaml.py /usr/src/app/dns-zone-from-yaml.py
ENTRYPOINT ["/usr/src/app/dns-zone-from-yaml.py"]
