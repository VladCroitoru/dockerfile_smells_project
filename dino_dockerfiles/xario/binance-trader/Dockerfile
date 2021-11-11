FROM python:3
ADD app/ /app
ADD balance.py /
ADD trader.py /
RUN pip install requests configargparse
ENV PYTHONUNBUFFERED 1
CMD [ "python", "./trader.py" ]