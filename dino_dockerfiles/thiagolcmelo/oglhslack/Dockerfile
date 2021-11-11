#use an official python runtime as a parent image

FROM python:2.7-slim

#set the working directory to /app
WORKDIR /app

#copy the current directory contents into the container at /app
ADD . /app

#install any needed packages specified in requeriments.txt
RUN pip install -r requirements.txt

#make port 80 available to the world outside this container
EXPOSE 80

#run test.py
CMD ["python", "oglhslack.py"]
