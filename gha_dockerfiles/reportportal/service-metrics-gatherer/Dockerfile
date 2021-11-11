FROM python:3.7.4

RUN apt-get update && apt-get install -y build-essential && \
    rm -rf /var/lib/apt/lists/*
RUN mkdir /backend/
WORKDIR /backend/

ADD requirements.txt requirements.txt

RUN python -m venv /venv \
    && /venv/bin/pip install -U pip \
    && LIBRARY_PATH=/lib:/usr/lib /bin/sh -c "/venv/bin/pip install --no-cache-dir -r requirements.txt"

RUN touch /venv/bin/activate

ARG version
ARG prod
ARG githubtoken

COPY ./ ./

RUN make test-all
RUN if [ "$prod" = "true" ]; then make release v=$version githubtoken=$githubtoken; else if [ "$version" != "" ]; then make build-release v=$version; fi ; fi

# Multistage
FROM python:3.7.4-slim
RUN apt-get update && apt-get -y upgrade && apt-get install -y libxml2 libgomp1 tzdata curl libpq5\
    && rm -rf /var/lib/apt/lists/*
COPY --from=0 /venv /venv

WORKDIR /backend/

COPY . .
COPY --from=0 /backend/VERSION /backend/.bumpversion.cfg ./
RUN rm -rf /backend/.git/

EXPOSE 5000

ENV FLASK_APP=main.py UWSGI_WSGI_FILE=main.py UWSGI_SOCKET=:3031 UWSGI_HTTP=:5000 UWSGI_VIRTUALENV=/venv UWSGI_MASTER=1 UWSGI_WORKERS=1 UWSGI_THREADS=1s UWSGI_LAZY_APPS=1 UWSGI_WSGI_ENV_BEHAVIOR=holy PYTHONDONTWRITEBYTECODE=1
ENV PATH="/venv/bin:${PATH}"
ENV PYTHONPATH="/backend"

# Start uWSGI
CMD ["/venv/bin/uwsgi", "--http-auto-chunked", "--http-keepalive"]
HEALTHCHECK --interval=1m --timeout=5s --retries=2 CMD ["curl", "-s", "-f", "--show-error", "http://localhost:5000/"]