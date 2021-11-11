FROM python:3.8

WORKDIR /fastapi-auth  

COPY . .

RUN pip install -r requirements.txt             

# ENTRYPOINT [ "bash", "docker-entrypoint.sh" ]

#CMD [ "bash", "docker-entrypoint.sh" ]

CMD ["uvicorn", "app.main:app", "--host=0.0.0.0"]  

# run with: sudo docker run --net=host image_name (runs on localhost)
# network_mode: "host" is equivalent ito --net=host in docker-compose (runs on localhost)

# koga definirame network za container/s-> in order to make the application externally visible (i.e. from outside the container) we add --host=0.0.0.0.
