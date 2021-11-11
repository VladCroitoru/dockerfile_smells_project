FROM python:3.9.5
LABEL MAINTAINER="ANJUL SAHU <anjulsahu@gmail.com>"

RUN pip3 install pipenv

WORKDIR /app
COPY . ./


# Establish the runtime user (with no password and no sudo)
RUN useradd -m demo
USER demo
ENV PATH $PATH:/home/demo/.local/bin

RUN . bin/activate
RUN pip3 install --user -r requirements.txt

CMD ["python3", "app.py"]
EXPOSE 5000
