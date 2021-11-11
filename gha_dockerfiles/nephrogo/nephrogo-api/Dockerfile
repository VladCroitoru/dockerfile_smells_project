FROM python:3.9
EXPOSE 8080

ENV PYTHONUNBUFFERED 1

RUN mkdir /srv/nephrogo-api
WORKDIR /srv/nephrogo-api

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ARG GIT_COMMIT
ARG GIT_BRANCH

LABEL branch=${GIT_BRANCH}
LABEL commit=${GIT_COMMIT}

ENV GIT_COMMIT=$GIT_COMMIT
ENV GIT_BRANCH=${GIT_BRANCH}

CMD ["/bin/sh", "start.sh"]