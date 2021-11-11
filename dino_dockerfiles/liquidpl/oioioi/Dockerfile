FROM debian:buster
ENV PYTHONUNBUFFERED 1

RUN useradd -m oioioi

COPY sudo.sh /tmp
RUN /tmp/sudo.sh

USER oioioi
WORKDIR /sio2

COPY build.sh /tmp
RUN /tmp/build.sh

COPY settings.py /sio2/deployment/settings.py
RUN sed -i 's/{{ PROJECT_DIR }}\/uwsgi.sock/0.0.0.0:9000/g' deployment/supervisord.conf

COPY wait-for-it.sh /sio2
COPY run.sh /sio2

EXPOSE 7888 7889 7890 9000 9999

CMD ["bash", "run.sh"]
