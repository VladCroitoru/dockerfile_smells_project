FROM ubuntu:trusty
MAINTAINER Benjamin Alan Weaver <baweaver@lbl.gov>
#
# Variables.
#
ENV testuser travis
ENV branch master
#
# Add a non-privileged user.
#
RUN adduser --disabled-password --gecos "" ${testuser}
RUN chown ${testuser}:${testuser} /home/${testuser}
#
# Tools needed
#
RUN apt-get update && apt-get -y install git python-scipy python-matplotlib python-pip
RUN pip install astropy 
RUN pip install git+https://github.com/weaverba137/pydl.git@${branch}
#
# Set user.
#
USER ${testuser}
WORKDIR /home/${testuser}
#
# Run test.
#
ENTRYPOINT ["/usr/bin/python"]
CMD ["-c", "import pydl; pydl.test(args='-r w', verbose=True)"]
