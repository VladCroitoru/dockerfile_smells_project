FROM python

RUN apt-get update && apt-get install -y libffi-dev libav-tools

COPY . /servoskull
WORKDIR /servoskull

RUN pip install -r requirements.txt
ENV SERVOSKULL_AVCONV=1

CMD python -m servoskull.client
