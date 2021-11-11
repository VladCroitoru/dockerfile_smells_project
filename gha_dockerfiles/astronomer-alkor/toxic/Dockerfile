FROM python:3.9

ARG CODE_PATH

ADD $CODE_PATH/requirements.txt /tmp/requirements.txt
RUN pip install --upgrade -r /tmp/requirements.txt

WORKDIR /code
ADD ./$CODE_PATH /code

CMD ["python", "-m", "src"]
