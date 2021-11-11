FROM ubuntu
RUN apt-get update -y && \
    apt-get upgrade -y
# install imagemagick
RUN apt-get install -y imagemagick
# install python
RUN apt-get install -y \
    python3.7 \
    python3-pip

COPY requirements.txt /app/requirements.txt
WORKDIR app
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app