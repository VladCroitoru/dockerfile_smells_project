FROM python:3.5

RUN mkdir app
ADD . /app
WORKDIR /app
RUN chmod +x ./start.sh

RUN ./start.sh
RUN pip install -r requirements.txt 
RUN pip install eventlet

EXPOSE 7001

ENTRYPOINT ["python", "api.py"]