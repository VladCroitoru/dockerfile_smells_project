FROM python:3-alpine

RUN pip install --no-cache-dir virtualenv

RUN adduser -D user
WORKDIR /home/user
USER user
RUN virtualenv venv

COPY requirements.txt /home/user/
RUN sh -c \
    ". venv/bin/activate ; pip install --no-cache-dir -r requirements.txt"

COPY . /home/user

CMD sh -c \
    ". venv/bin/activate ; python main.py"
