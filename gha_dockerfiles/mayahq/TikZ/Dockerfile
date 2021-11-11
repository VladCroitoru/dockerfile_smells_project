# To start the container run:
# sudo docker build -t graphics .&&sudo docker run -p 4000:80 graphics
# To get a shell into the container run:
# sudo docker exec -it `sudo docker ps|grep graphics|tail -n 1|awk '{print $1}'` /bin/bash

# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# matplotlib nonsense
RUN apt-get update && apt-get install -y build-essential
RUN apt-get install -y --no-install-recommends tk-dev

RUN apt-get install -y libcairo2-dev

# Sketch
RUN apt-get install  -y bison flex
RUN mkdir -p /usr/share/man/man1
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y  software-properties-common && \
    add-apt-repository ppa:webupd8team/java -y  && \
    apt-get update && \
    echo oracle-java7-installer shared/accepted-oracle-license-v1-1 select true | /usr/bin/debconf-set-selections && \
    apt-get install -y --allow-unauthenticated oracle-java8-installer && \
    apt-get clean
RUN cd TikZ/sketch-1.7.5/sketch-backend && chmod +x configure && ./configure && make && cd ../sketch-frontend && chmod +x ./sketch && ./sketch test/sk/seq/miniTest1.sk
ENV PATH="/app/TikZ/sketch-1.7.5/sketch-frontend:${PATH}"

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt
RUN pip install http://download.pytorch.org/whl/cpu/torch-0.4.0-cp27-cp27mu-linux_x86_64.whl
RUN pip install torchvision
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]