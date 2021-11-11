FROM ubuntu:trusty

MAINTAINER tony.hirst@gmail.com

# Install Headless JRE after updating installed packages.
RUN apt-get update && apt-get install -y openjdk-7-jre-headless wget
RUN apt-get clean

RUN wget --no-check-certificate https://github.com/OpenRefine/OpenRefine/releases/download/2.6-beta.1/openrefine-linux-2.6-beta.1.tar.gz 

RUN tar -xzf openrefine-linux-2.6-beta.1.tar.gz  && rm openrefine-linux-2.6-beta.1.tar.gz


EXPOSE 3333
RUN mkdir /mnt/refine
CMD ["openrefine-2.6-beta.1/refine", "-i", "0.0.0.0", "-d", "/mnt/refine"]