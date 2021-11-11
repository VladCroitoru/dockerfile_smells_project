FROM python:3.6.3

RUN mkdir /opt/sumo

ENV K8S_API_URL ""
ENV SUMO_HTTP_URL ""
ENV RUN_TIME 60

RUN pip install --upgrade pip requests

COPY extract-data.py /opt/sumo/

CMD ["python", "/opt/sumo/extract-data.py"]
