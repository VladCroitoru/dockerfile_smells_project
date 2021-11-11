FROM python:3.8

#RUN apt-get update
#RUN apt-get install git

RUN mkdir /app_flask
RUN rm /app_flask
RUN cp /app_flask /app_flask.back
WORKDIR /app_flask

COPY ./server.py ./
COPY ./requirements.txt ./
#COPY ./run_server.sh ./
#
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt

##CMD ["python", "manage.py", "runserver", "0:${PORT}"]
#CMD ["./run_server.sh"]

# <CMD> <ARGS>
CMD ["python", "server.py"]
