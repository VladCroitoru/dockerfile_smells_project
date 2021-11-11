# DockerFile, Image, Container
FROM python:3.8

WORKDIR /monty-hall-app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src

CMD [ "python", "./src/main.py" ]

# build docker image. Image located in root so use "." to specify path at end of command
# docker build -t python-monty-hall .

# run docker container with given name
# docker run python-monty-hall