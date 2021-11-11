FROM python:alpine3.6

ADD agent.py requirements.txt /app/
WORKDIR /app/

RUN pip3 install -r requirements.txt
RUN chmod a+x agent.py

ENTRYPOINT ["/app/agent.py"]
