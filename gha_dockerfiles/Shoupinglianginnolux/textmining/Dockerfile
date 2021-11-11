FROM matthewfeickert/docker-python3-ubuntu
ENV PYTHONUNBUFFERED=1
USER root
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
COPY resolv.conf /etc/