FROM alpine:3.1

RUN apk add python3 --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted
RUN apk add python3-dev build-base --update-cache --repository http://dl-3.alpinelinux.org/alpine/edge/testing/ --allow-untrusted

RUN apk add --update libxslt-dev
RUN apk add --update libxml2-dev
RUN apk add git

RUN python3 --version
RUN pip3 --version

RUN git clone https://github.com/cpfair/tapiriik.git

WORKDIR /tapiriik
RUN pip3 install -r requirements.txt
RUN cp tapiriik/local_settings.py.example tapiriik/local_settings.py
RUN python3 credentialstore_keygen.py >> tapiriik/local_settings.py

EXPOSE 8000

RUN echo MONGO_HOST = \"mongo\" >> tapiriik/local_settings.py
RUN echo REDIS_HOST = \"redis\" >> tapiriik/local_settings.py
RUN echo RABBITMQ_BROKER_URL = \"amqp://guest@rabbitmq//\" >> tapiriik/local_settings.py

CMD python3 manage.py runserver 0.0.0.0:8000
