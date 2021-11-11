FROM progrium/busybox

ADD https://github.com/michaelsauter/crane/releases/download/v1.1.1/crane_linux_amd64 /usr/local/bin/crane 
ADD https://get.docker.com/builds/Linux/x86_64/docker-latest /usr/local/bin/docker

RUN chmod +x /usr/local/bin/docker && chmod +x /usr/local/bin/crane

ENTRYPOINT ["/usr/local/bin/crane"]
