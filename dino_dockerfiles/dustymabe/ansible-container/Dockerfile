FROM fedora:24

LABEL RUN="docker run -it --rm -v \${PWD}:/work/ -e DOCKER_HOST \$IMAGE"
RUN dnf install --setopt=tsflags=nodocs -y gcc redhat-rpm-config python python-devel libffi-devel openssl-devel ansible
COPY ./ /ansible-container/
RUN cd /ansible-container && pip install -r requirements.txt
RUN cd /ansible-container && python ./setup.py install

VOLUME ["/work"]
WORKDIR "/work"

ENTRYPOINT ["ansible-container"]
CMD ["help"]
