# Dockerfile for batchcutencode

FROM ubuntu:18.04

WORKDIR /app

ADD src/ /app/
RUN chmod +x /app/launch.sh
RUN chmod +x /app/cutnotify.sh
RUN chmod +x /app/encodenotify.sh
RUN mkdir -p /transcode
#RUN mkdir -p /transcode/cut
#RUN mkdir -p /transcode/encode
#RUN mkdir -p /transcode/complete

RUN apt-get update && apt-get install -y ffmpeg handbrake-cli python3 inotify-tools

# Install any needed packages specified in requirements.txt
#RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Run app.py when the container launches 
#ENTRYPOINT ["/bin/bash", "-c", "/app/launch.sh"]
CMD ["bash", "/app/launch.sh"]
