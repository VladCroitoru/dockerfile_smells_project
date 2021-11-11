FROM python:3-alpine@sha256:bd7f0719874c7de4ca47418de143ab4de79731dc0b01fdcf2425b8a32f4823ce
RUN mkdir -p /usr/local/src/cwm-worker-ingress
WORKDIR /usr/local/src/cwm-worker-ingress
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY setup.py .
COPY cwm_worker_ingress ./cwm_worker_ingress
RUN pip install -e .
ENTRYPOINT ["cwm_worker_ingress"]
CMD ["vdns", "53"]
