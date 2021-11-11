FROM python:3

ENV DOCKERIZE_VERSION v0.6.1

RUN apt-get update \
    && apt-get install -y git ca-certificates wget \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /tmp/* /var/tmp/* \
    && rm -rf /var/lib/apt/lists/*

RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-linux-amd64-$DOCKERIZE_VERSION.tar.gz

RUN git clone https://github.com/Netflix/flamescope /usr/src/app

WORKDIR /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

COPY config.py.tmpl app/config.py.tmpl

EXPOSE 5000
CMD [ "dockerize", "-template", "./app/config.py.tmpl:./app/config.py", "python", "run.py" ]
