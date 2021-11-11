FROM python:3.9

WORKDIR /home

ENV HOME /home
ENV PYTHONPATH /home/src

COPY . .

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD python src/main.py $PORT