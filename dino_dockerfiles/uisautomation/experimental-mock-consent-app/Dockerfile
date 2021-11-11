FROM python:3.6

WORKDIR /usr/src/app
ADD ./requirements.txt ./
RUN pip install -r ./requirements.txt

ADD ./ ./

ENV FLASK_DEBUG=1 FLASK_APP=app.py
EXPOSE 8090

ENTRYPOINT ["flask"]
CMD ["run", "-h", "0.0.0.0", "-p", "8090"]
