FROM alpine
MAINTAINER Rodrigo Del Monte <rodrigo.dexter@gmail.com>

COPY requirements.txt /tmp/requirements.txt
RUN apk add --no-cache py2-pip \
    && pip install --upgrade pip \
    && pip install flask \
    && pip install -r /tmp/requirements.txt

ENV APP_DIR /app
ENV FLASK_APP app.py
RUN mkdir ${APP_DIR}
COPY app ${APP_DIR}

VOLUME ${APP_DIR}
EXPOSE 5000

# Cleanup
RUN rm -rf /.wh /root/.cache /var/cache /tmp/requirements.txt

WORKDIR ${APP_DIR}
CMD ["/usr/bin/flask", "run", "--reload", "-h", " 0.0.0.0"]