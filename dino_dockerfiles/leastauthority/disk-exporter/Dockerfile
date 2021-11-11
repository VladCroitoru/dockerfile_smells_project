FROM leastauthority/base

# Mount something like /proc/1/ns here.
VOLUME /ns

EXPOSE 9000

COPY requirements.txt /disk-exporter/requirements.txt

RUN /app/env/bin/pip install --requirement /disk-exporter/requirements.txt

COPY . /disk-exporter

RUN /app/env/bin/pip install --no-index /disk-exporter

ENTRYPOINT ["/app/env/bin/twist", "disk-exporter"]
CMD ["--host-mount-namespace", "/ns/mnt"]
