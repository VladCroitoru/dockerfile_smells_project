# Production image. Runs a Gunicorn WSGI server.
FROM minio/mc AS mc
FROM python:3.7-slim
ARG GIT_SHA
LABEL org.opencontainers.image.title Stager production
LABEL org.opencontainers.image.authors https://ccm.sickkids.ca/
LABEL org.opencontainers.image.source https://github.com/ccmbioinfo/stager
LABEL org.opencontainers.image.vendor Centre for Computational Medicine
LABEL org.opencontainers.image.revision ${GIT_SHA}
ENV GIT_SHA=${GIT_SHA}
WORKDIR /usr/src/stager
# Install PyPI prod-only packages first and then copy the MinIO client as the latter updates more frequently
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY --from=mc /usr/bin/mc /usr/bin/mc
COPY . .
ENV FLASK_ENV production
EXPOSE 5000
# Prevent accidentally using this image for development by adding the prod server arguments in the entrypoint
ENTRYPOINT ["gunicorn", "wsgi:app", "--bind", "0.0.0.0:5000", "--access-logfile", "-", "--log-file", "-"]
CMD ["--preload", "--workers", "2", "--threads", "2"]
