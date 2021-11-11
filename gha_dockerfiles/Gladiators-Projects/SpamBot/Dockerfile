
FROM python:3.8.5-slim-buster

WORKDIR /root/spambot

RUN chmod 777 /root/spambot

RUN sudo apt-get update
RUN sudo apt install upgrade -y 

RUN pip3 install --upgrade pip setuptools

# Docker work

RUN git clone https://github.com/Gladiators-Projects/spambot /root/spambot

COPY ./spambot/sample_config.py ./spambot/config.py* /root/spambot/spambot/


# Install requirements
RUN pip3 install --no-cache-dir -U -r requirements.txt

# Bolo jai Ramji ki , Shero wali mata ki jai , Namo namo parvati pate har har mahadev

CMD ["python3","-m","spambot"]
