FROM python:alpine
COPY ./requirements.txt /exporter/requirements.txt
RUN pip install -r /exporter/requirements.txt
COPY . /exporter
EXPOSE 8080
CMD ["python", "/exporter/monitor.py"]
