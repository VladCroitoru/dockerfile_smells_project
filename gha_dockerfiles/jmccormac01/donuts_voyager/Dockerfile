# get a basic python image
FROM python:3.9-slim-buster

# set up Tini to hand zombie processes etc
ENV TINI_VERSION="v0.19.0"
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /tini
RUN chmod +x /tini

# set the timezone for the current installation
RUN echo "Australia/NSW" > /etc/timezone
RUN dpkg-reconfigure -f noninteractive tzdata

# keep setup tools up to date
RUN pip install -U \
    pip \
    setuptools \
    wheel

# set a working directory
WORKDIR /donuts

# make a new user
RUN useradd -m -r donuts && \
    chown donuts /donuts

# install requirements first to help with caching
COPY requirements.txt ./
RUN pip install -r requirements.txt

# copy from current dir to workdir
COPY . .

# stop things running as root
USER donuts

# add entry points
ENTRYPOINT ["/tini", "--"]

# start the code once the container is running
CMD python voyager_donuts.py
