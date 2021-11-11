FROM python:3.4
MAINTAINER Patrick G. <patrick.pollo.guilbert@gmail.com>

ENV version 0.2

WORKDIR /weathermost

ADD https://github.com/patoupatou/weathermost/archive/v${version}.tar.gz .

RUN pip install flask requests\
    && tar xvfz v${version}.tar.gz \
    && rm v${version}.tar.gz \
    && mv weathermost-${version} weathermost

EXPOSE 5000

VOLUME /weathermost/

ENTRYPOINT ["python", "weathermost/bot.py"]
