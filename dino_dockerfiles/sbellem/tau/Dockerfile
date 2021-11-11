FROM python:3.4.3
MAINTAINER Sylvain Bellemare <sbellem@gmail.com>

RUN apt-get install -y libfreetype6-dev pkg-config
RUN pip install ipython jinja2 jsonschema matplotlib numpy pyzmq tornado

EXPOSE 8888
CMD ipython notebook --ip=0.0.0.0 --no-browser
