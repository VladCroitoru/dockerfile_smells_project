FROM python:2.7-alpine

LABEL maintainer "Mark J. Becker <mjb@marb.ec>"

# Add dependencies
RUN apk add --update gcc g++ musl-dev

# Install locust
RUN pip install locustio pyzmq

# Create working directoy
RUN mkdir locust
WORKDIR locust

# Expose locust web ui port
EXPOSE 8089

# Set locust as entrypoint
ENTRYPOINT ["locust"]