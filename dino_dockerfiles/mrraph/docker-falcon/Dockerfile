FROM mrraph/docker-python

RUN apk --update add python py-pip openssl ca-certificates py-openssl wget

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
ONBUILD COPY . /usr/src/app/

RUN apk --update add --virtual build-dependencies libffi-dev openssl-dev python-dev py-pip build-base \
  && pip install --upgrade pip \
  && pip install falcon supervisor-stdout gunicorn

ONBUILD RUN pip install -r /usr/src/app/requirements.txt \
  && apk del build-dependencies


#ONBUILD COPY my_runonce /etc/my_runonce
#ONBUILD COPY my_runalways /etc/my_runalways
