FROM python:3.6

# Install python requirements
RUN pip install --upgrade pip # ensure latest pip
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
RUN rm -f /tmp/requirements.txt

RUN mkdir /usr/app

COPY ./* /usr/app/

WORKDIR /usr/app

CMD python main.py