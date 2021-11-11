FROM python:3

LABEL maintainer="mhrznamn068@gmail.com"

ENV PYTHONUNBUFFERED=1

WORKDIR /opt/snake11235

COPY ./requirements.txt /opt/snake11235

RUN pip install -r requirements.txt

COPY ./NextGen /opt/snake11235 

ENTRYPOINT [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
