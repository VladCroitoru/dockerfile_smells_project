FROM python:3.7

LABEL author="Taras Mazurak"
LABEL e-mail="xperia.t.mazurak@gmail.com"
LABEL version="0.0.1b"

ENV PYTHONDONTWRITEBYTECODE 1
ENV FLASK_APP "blog.py"
# ENV FLASK_ENV "development"
ENV FLASK_DEBUG False
# ENV C_FORCE_ROOT true

RUN mkdir /jwtblog
WORKDIR /jwtblog

RUN pip install --no-cache-dir --upgrade pip

COPY ./requirements.txt /jwtblog/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ADD . /jwtblog

EXPOSE 5000
CMD flask run --host=0.0.0.0
