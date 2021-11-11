FROM alpine

MAINTAINER "James Hodgkinson <yaleman@ricetek.net>"
LABEL maintainer "James Hodgkinson <yaleman@ricetek.net>"
LABEL description="A tiny docker image to expose a Flask-based website to show how HTTP verbs work."

# handy environment variables
#ENV DEBIAN_FRONTEND noninteractive
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV FLASK_APP=/opt/app/index.py  
ENV FLASK_DEBUG=1

# install the ubuntu packages
RUN apk add --no-cache python3 
RUN python3 -m ensurepip &&  rm -r /usr/lib/python*/ensurepip
RUN pip3 install --upgrade pip setuptools && rm -r /root/.cache


# installs the required python packages
COPY requirements.txt /tmp/requirements.txt
RUN pip3 install -r /tmp/requirements.txt

# copy the flask file
COPY app /opt/app

# make sure you expose this on run
EXPOSE 80
# make the magic happen
ENTRYPOINT ["python3","-m", "flask","run","--host=0.0.0.0", "--port=80"]

HEALTHCHECK --interval=1m --timeout=1s  CMD curl -f http://localhost/ || exit 1