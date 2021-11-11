# To build this docker image run the following command from directory containing Dockerfile:
#     docker build -t isoenum .

FROM fedora:30

MAINTAINER	Andrey Smelter

# Copy isoenum code to the root directory and set working directory
COPY . /isoenum/
WORKDIR /isoenum

# Install python
RUN dnf update -y
RUN dnf install python3 -y
RUN dnf install python3-pip -y

# Install Open Babel
RUN dnf install openbabel -y

# Install isoenum python requirements
RUN pip3 install -r /isoenum/requirements.txt

# Set entry point
ENTRYPOINT [ "python3", "-m", "isoenum" ]