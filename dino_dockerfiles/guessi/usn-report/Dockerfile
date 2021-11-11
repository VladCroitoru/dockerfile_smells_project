FROM python:3.9-slim
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
ADD report-gen.py report-send.py /opt/
WORKDIR /opt/
