FROM opendap/besd:3.20.8-260

RUN yum -y update && \
    yum -y upgrade

RUN yum install -y centos-release-scl

# Adding a user
RUN adduser worker
RUN yum install -y nano && \
    yum install -y wget
USER worker
WORKDIR /home/worker
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-py38_4.8.2-Linux-x86_64.sh && \
    bash Miniconda3-py38_4.8.2-Linux-x86_64.sh -b && \
    rm Miniconda3-py38_4.8.2-Linux-x86_64.sh

ENV HOME="/home/worker" PATH="/home/worker/miniconda3/bin:${PATH}"


RUN pip install ipython &&\
    pip install pytest

RUN mkdir $HOME/build

ENV BUILD=$HOME/build

#--chown=<user>:<group> <hostPath> <containerPath>
COPY --chown=worker setup.py requirements*txt $BUILD/
RUN pip install -r $BUILD/requirements.txt
COPY --chown=worker dmrpp_generator $BUILD/dmrpp_generator
COPY --chown=worker generate_dmrpp.py $BUILD/generate_dmrpp.py
COPY --chown=worker tests $BUILD/tests



RUN \
  cd $BUILD; \
  python setup.py install


WORKDIR $BUILD

RUN pytest --junitxml=./test_results/test_dmrpp_generator.xml tests && \
    rm -rf tests

CMD ["python", "generate_dmrpp.py"]
ENTRYPOINT []


