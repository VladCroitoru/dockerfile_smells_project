FROM python:3.8

ADD src /app/src
ADD requirements.txt /app
ADD main.py /app

WORKDIR /app

ENV DB_HOSTNAME={DB_HOSTNAME}
ENV DB_USERNAME={DB_USERNAME}
ENV DB_PASSWORD={DB_PASSWORD}
ENV DB_DATABASE={DB_DATABASE}
ENV JWT_SECRET={JWT_SECRET}
ENV ENV={ENV}

RUN pip install --upgrade pip && \
pip install -r ./requirements.txt

RUN pytest

EXPOSE 80

CMD ["python3", "main.py"]
