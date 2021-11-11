FROM nginx:1.7.8

MAINTAINER Adrien Folie <folie.adrien@gmail.com>

# Install curl
RUN apt-get update -qq && \
    apt-get install -qy curl

# Set EnvPlate version
ENV ENVPLATE 0.0.4

# Install EnvPlate
RUN curl -sLo /usr/local/bin/ep https://github.com/kreuzwerker/envplate/releases/download/v$ENVPLATE/ep-linux && \
    chmod +x /usr/local/bin/ep

# Copy files in the image
COPY . .

# Add volume for ssl certificates
VOLUME /certs

# Launch EnvPlate then Nginx
ENTRYPOINT ["./run.sh"]
