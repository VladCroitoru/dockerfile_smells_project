FROM python:3.9-alpine

#GCC COMPILER FOR "Building wheel for numpy (PEP 517)"
RUN apk add gcc libc-dev

#BOTS
COPY bots/reply/ what-sentiment-bot/bots/reply/
COPY bots/utils/ what-sentiment-bot/bots/utils/
COPY bots/config.py what-sentiment-bot/bots/
#ML
COPY ml/    what-sentiment-bot/ml/

#RUN ENVIROMENT
COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt

#COMMANDS
CMD ["python3", "what-sentiment-bot/bots/reply/reply.py"]