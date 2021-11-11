
FROM python:3.8
#install python 3.8

COPY . .
#copy project from current directory

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE $PORT
#open up port 5000 on the docker container

CMD python3 flask_server.py $PORT