FROM python:3.6-slim

RUN apt-get clean \
    && apt-get -y update
RUN apt-get -y install python3-dev \
    && apt-get -y install python-pip 

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 4000
ENTRYPOINT [ "python3" ]
CMD [ "run.py" ]


# RUN chmod +x ./run.py
# CMD ["./run.py"] 