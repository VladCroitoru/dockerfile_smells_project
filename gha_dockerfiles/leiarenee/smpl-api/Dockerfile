# STAGE 1: Build Stage - Build and Install python3
FROM public.ecr.aws/amazonlinux/amazonlinux AS python-builder
RUN yum update -y && yum groupinstall "Development Tools" -y
RUN yum install wget openssl-devel libffi-devel bzip2-devel -y
ARG PYTHON_VERSION
ARG PYTHON_COMMAND
RUN wget https://www.python.org/ftp/python/${PYTHON_VERSION}/Python-${PYTHON_VERSION}.tgz \
 && tar xvf Python-${PYTHON_VERSION}.tgz
RUN cd Python-${PYTHON_VERSION} && ./configure --enable-optimizations && make altinstall

# Install Python packages
WORKDIR /app
ADD requirements.txt .
RUN pip$PYTHON_COMMAND install -r requirements.txt

# Setup environment 
EXPOSE 8000
ENV PYTHONPATH=src
WORKDIR /app
ADD . .

# Set Entry Point command
ENTRYPOINT [ "./entrypoint.sh" ]
# Set Arguments
CMD [ "python3.9", "-m", "flaskapi" ]





