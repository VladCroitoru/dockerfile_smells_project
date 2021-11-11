# Pull base image
FROM python:3.8

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8888

# RUN apt-get update -y
# RUN apt-get install -y  binutils libproj-dev gdal-bin  redis-server  postgresql

# create and set working directory
RUN mkdir /code
WORKDIR /code

# Add current directory code to working directory
ADD . /code/

# ssh
ENV SSH_PASSWD "root:Docker!"
# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends dialog \
    && apt-get update \
    && apt-get install -y --no-install-recommends openssh-server \
    python3-pip \
    python3-dev \
    git \
    build-essential \
    binutils \ 
    libproj-dev \ 
    gdal-bin \ 
    redis-server\ 
    && \
    apt-get clean && \
    echo "$SSH_PASSWD" | chpasswd \
    && rm -rf /var/lib/apt/lists/*

COPY sshd_config /etc/ssh/
COPY init.sh /usr/local/bin/

RUN chmod u+x /usr/local/bin/init.sh


# Install dependencies
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


EXPOSE 8888 2222

ENTRYPOINT ["init.sh"]
# CMD gunicorn deeptech.wsgi:application --bind 0.0.0.0:$PORT
