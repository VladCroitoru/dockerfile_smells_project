FROM python:3

ADD requirements.txt tmp/requirements.txt
ADD server service

RUN pip3 install -r /tmp/requirements.txt

EXPOSE 8080

VOLUME ["/data"]
ENV SERVER_PORT=8080
ENV LOG_MODE=json
ENV DEBUG_MODE=0
ENV SQLALCHEMY_DATABASE_URI=sqlite:////data/db.sqlite
ENV SECRET_KEY=change_me!

ENTRYPOINT ["hug", "-f", "/service/main.py"]