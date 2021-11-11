FROM continuumio/miniconda3

MAINTAINER B. Arman Aksoy <arman@aksoy.org>

# Setup our working environment
WORKDIR /epi
# Create the folder where we will saving submissions
RUN mkdir -p submissions

# This is where the source code will go
ADD . epidisco-web
WORKDIR epidisco-web

# Install tools required to get ready for the production
RUN apt-get update \
      && apt-get install -y npm \
      && apt-get install -y libpq-dev
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash -
RUN apt-get install -y nodejs

# Install dependencies
RUN pip install -r requirements.txt
RUN npm install

# Bundle the Javascript file
RUN npm run bundle

# Clean up
RUN apt-get remove -y npm nodejs
RUN apt-get autoremove -y
RUN rm -rf node_modules

# We will be serving this Flask app through gunicorn
RUN pip install gunicorn
ENTRYPOINT ["gunicorn", "autoapp:app"]
