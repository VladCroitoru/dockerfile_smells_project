# Select the base Image
FROM alpine:3.14

# Since this is alpine we need to use apk instead of apt-get (since this is Ubuntus package manager)
RUN apk update
RUN apk add build-base
RUN apk add python3-dev
RUN python3 -m ensurepip --upgrade
RUN pip3 install -U pip
# RUN pip3 install requests

# Define the container work dir
WORKDIR /src
# Copy all contents of the current folder
ADD src/ ./
ADD pythonRequirements.txt ./

RUN pip install --no-cache-dir -r pythonRequirements.txt

# Run command for example inside container
CMD python3 run.py
# Alternative entrypoint
# ENTRYPOINT ["sh"]
