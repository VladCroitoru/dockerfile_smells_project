FROM python:3.6-stretch

LABEL maintainer="getjamesbatt@gmail.com"

RUN pip install pipenv==9.1.0
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash - > /dev/null
RUN apt install -y nodejs

# pipenv hardcodes the path to these binaries.
RUN ln -s /usr/local/bin/pip /bin/pip
RUN ln -s /usr/local/bin/python /bin/python
