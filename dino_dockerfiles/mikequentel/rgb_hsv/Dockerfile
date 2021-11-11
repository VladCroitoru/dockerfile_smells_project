# Dockerfile for running rgbhsv.py
# Many thanks to Fábio Rehm for his blog post: Running GUI Apps with Docker
# http://fabiorehm.com/blog/2014/09/11/running-gui-apps-with-docker/

FROM debian
RUN apt-get update
RUN apt-get install -qqy x11-apps python python-tk
RUN export uid=1000 gid=1000 && \
mkdir -p /home/developer && \
mkdir -p /etc/sudoers.d && \
echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
echo "developer:x:${uid}:" >> /etc/group && \
echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
chmod 0440 /etc/sudoers.d/developer && \
chown ${uid}:${gid} -R /home/developer
USER developer
WORKDIR /usr/src/app
# COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "./rgbhsv.py"]
