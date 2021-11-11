FROM alpine:latest
MAINTAINER Antonios A. Chariton <daknob@daknob.net>

# Install python and pip
RUN apk add --update python py-pip
RUN pip install --upgrade pip setuptools

# Install a production web server
RUN pip install gunicorn

# Move all code inside the image
RUN mkdir /shortor
COPY . /shortor/.

# Switch to the new directory
WORKDIR /shortor

# Install all the project requirements
RUN pip install -r requirements.txt

# Expose HTTP tcp/80
EXPOSE 80

# Expose volume for link persistence
VOLUME ["/shortor/links"]

# Run the web server
CMD ["gunicorn", "-w", "8", "-b", "0.0.0.0:80", "shortor:app", "gunicorn-scripts"]
