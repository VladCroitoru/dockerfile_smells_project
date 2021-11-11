# Base OS (Host)
FROM ubuntu:20.10 AS base

# Verify that all packages are up-to-date
RUN apt update -y

# In our host OS
FROM base AS builder

# Compile the source code
RUN apt -y install clang-11 lldb-11 lld-11
RUN apt -y install clang
RUN apt -y install util-linux wget
RUN apt -y install unzip make
RUN apt update -y

# Install python and pip
RUN apt -y install python3
RUN apt -y install python3-pip

# Download the CarlSAT git repo:
RUN wget https://github.com/JBontes/CarlSAT_2021/archive/refs/heads/main.zip
RUN ls main.zip | xargs -n1 unzip
RUN cd CarlSAT_2021-main/
# Compile the source
RUN make clean && make

# Fork a new image from the base...
FROM base as exec
# Add the CarlSAT program
COPY --from=builder /CarlSAT_2021-main/CarlSAT .

# Copy project source files and dependency list to container
COPY ./HyperOpt/src/*.py .
COPY ./requirements.txt .
# Install dependencies
RUN pip3 install -r requirements.txt

# Run the experiment and copy the log file to the host
CMD python3 mytest.py >> output.log && cp output.log /host/output.log
