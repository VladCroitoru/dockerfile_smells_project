FROM python:3-bullseye

WORKDIR /opt/corscanner

COPY . .

RUN apt-get update && \
    apt-get upgrade --yes && \
    pip install --no-cache-dir -r requirements.txt && \
    rm --recursive --force /var/lib/apt/lists/* && \
    chmod +x cors_scan.py && \
    ln --symbolic /opt/corscanner/cors_scan.py /usr/local/bin/corscanner && \
    ln --symbolic corscanner /usr/local/bin/cors_scan

ENTRYPOINT ["corscanner"]

CMD ["-h"]
