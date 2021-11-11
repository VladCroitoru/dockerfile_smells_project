FROM python:3.4
MAINTAINER Vincent Fretin <vincentfretin@ecreall.com>

RUN mkdir -p /app/var
COPY . /app/
RUN addgroup --quiet --gid "1000" "u1000" && \
    adduser \
        --shell /bin/bash \
        --disabled-password \
        --force-badname \
        --no-create-home \
        --uid "1000" \
        --gid "1000" \
        --gecos '' \
        --quiet \
        --home "/app" \
        "u1000"
WORKDIR /app
RUN pip install -r requirements.txt
RUN chown -R u1000:u1000 /app
USER u1000

EXPOSE 5000
VOLUME /app/var

CMD ["python", "main.py"]
