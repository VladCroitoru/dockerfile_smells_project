from ubuntu:14.04.1
maintainer Shipyard Project "http://edustack.org"
run apt-get update
run apt-get install -y docker.io
run ln -sf /usr/bin/docker.io /usr/local/bin/docker
run sed -i '$acomplete -F _docker docker' /etc/bash_completion.d/docker.io
run ["/bin/bash", "-c", "source /etc/bash_completion.d/docker.io"]
add run.sh /usr/local/bin/run
entrypoint ["/usr/local/bin/run"]
