FROM ubuntu:14.04

ENV QT_X11_NO_MITSHM=1

RUN apt-get update && apt-get install -y software-properties-common build-essential cmake wget \

    && apt-get update && apt-add-repository -y "deb http://apt.isis.rl.ac.uk trusty main" \

    && add-apt-repository -y ppa:mantid/mantid && apt-get update -y



RUN wget http://netcologne.dl.sourceforge.net/project/mantid/developer/mantid-developer-1.2.4.deb -P /opt \

    && dpkg -i /opt/mantid-developer-1.2.4.deb; apt-get -fy install && dpkg -i /opt/mantid-developer-1.2.4.deb \

    && git clone https://github.com/mantidproject/mantid.git /opt/Mantid


RUN (cd /opt/Mantid && cmake .)
RUN make -C /opt/Mantid

# Replace 1000 with your user / group id
RUN export uid=1000 gid=1000 && \
   mkdir -p /home/developer && \
   echo "developer:x:${uid}:${gid}:Developer,,,:/home/developer:/bin/bash" >> /etc/passwd && \
   echo "developer:x:${uid}:" >> /etc/group && \
   echo "developer ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/developer && \
   chmod 0440 /etc/sudoers.d/developer && \
   chown ${uid}:${gid} -R /home/developer

USER developer
ENV HOME /home/docker_gui
CMD /opt/Mantid/bin/MantidPlot
