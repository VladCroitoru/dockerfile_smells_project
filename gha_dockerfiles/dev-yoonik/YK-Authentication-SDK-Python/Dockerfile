FROM python:3.7-slim-stretch

RUN apt-get -y update

RUN apt-get install -y --fix-missing \
    build-essential \
    cmake \
    gfortran \
    git \
    wget \
    curl \
    graphicsmagick \
    libgraphicsmagick1-dev \
    libatlas-dev \
    libavcodec-dev \
    libavformat-dev \
    libgtk2.0-dev \
    libjpeg-dev \
    liblapack-dev \
    libswscale-dev \
    pkg-config \
    python3-dev \
    python3-numpy \
    software-properties-common \
    zip \
    && apt-get clean && rm -rf /tmp/* /var/tmp/*

RUN mkdir /release

# Set the working directory to /release
WORKDIR /release

# Copy the project directory contents into the container at /release
ADD . /release/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make API port available to the world outside this container
EXPOSE 3031

# Run app when the container launches
CMD ["python", "app.py"]