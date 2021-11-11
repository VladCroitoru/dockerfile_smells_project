FROM python:3.9-alpine3.12 AS pyopenssl-builder

RUN apk update && apk add --no-cache gcc musl-dev openssl-dev openssl libffi-dev

WORKDIR /tmp

COPY code/requirements.base.txt .
RUN pip install -r requirements.base.txt

# ---

FROM python:3.9-alpine3.12

ARG GIT_BRANCH
ARG GIT_COMMIT_ID
ARG GIT_BUILD_TIME
ARG GITHUB_RUN_NUMBER
ARG GITHUB_RUN_ID

LABEL git.branch=${GIT_BRANCH}
LABEL git.commit.id=${GIT_COMMIT_ID}
LABEL git.build.time=${GIT_BUILD_TIME}
LABEL git.run.number=${GITHUB_RUN_NUMBER}
LABEL git.run.id=${TRAVIS_BUILD_WEB_URL}

COPY --from=pyopenssl-builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

COPY code/ LICENSE /opt/nuvlabox/

WORKDIR /opt/nuvlabox/

RUN apk add --no-cache curl

RUN pip install -r requirements.txt

VOLUME /srv/nuvlabox/shared

ONBUILD RUN ./license.sh

ENTRYPOINT ["./run.py"]
