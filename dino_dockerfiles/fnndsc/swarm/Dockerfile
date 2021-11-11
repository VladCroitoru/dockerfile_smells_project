# Docker file for the swarm manager

FROM fnndsc/ubuntu-python3:latest
MAINTAINER fnndsc "dev@babymri.org"

ENV APPROOT="/usr/src/swarm"  VERSION="0.1"
COPY ["swarm.py", "test_swarm.py", "requirements.txt", "${APPROOT}/"]

WORKDIR $APPROOT

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]
CMD ["swarm.py", "--help"]