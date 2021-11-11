FROM python:3.6



# This is something I like to do as it adds the Dockerfile to the image for easy reverse engineering
ADD . /


RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python", "-u", "ecs-service-count.py" ]
