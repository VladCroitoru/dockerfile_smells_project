FROM python:3.7

LABEL MAINTAINER=rafa.molitoris@gmail.com

# Time zone
ENV TZ=Europe/Zurich
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

ADD ./requirements.txt .
RUN pip install -r requirements.txt

# Change to non-root user (for CaaS)
RUN  adduser -u 1000 --system worker
USER 1000

ADD --chown=1000 ./logging.conf .

# Copy source code into container
ADD --chown=1000 ./metadata_registration_api /metadata_registration_api
WORKDIR /

EXPOSE 8000

CMD ["gunicorn", \
        "--workers", "8", \
        "--worker-class", "gevent", \
        "--worker-connections", "1000", \
        "--bind", "0.0.0.0", \
        "--timeout", "240", \
        "--preload", \
        "--log-config", "/logging.conf", \
        "metadata_registration_api.app:create_app()"]

