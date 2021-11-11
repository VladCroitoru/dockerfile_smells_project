FROM alpine:latest
MAINTAINER Antonios A. Chariton <daknob@daknob.net>

# Install Python and pip
RUN apk add --update python py-pip

# Install a production wsgi web server
RUN pip install gunicorn

# Move code to container
RUN mkdir /gh
COPY . /gh/.

# Change Directory to code path
WORKDIR /gh

# Install the required software to run the app
RUN pip install -r requirements.txt

# Expose port 80 to make the service accessible
EXPOSE 80

# Some default environment variables
# You should override them when running
ENV GH_USER devstaff-crete
ENV GH_REPO devstaff-heraklion
ENV GH_ISSUE_LABEL topics
ENV GH_ISSUE_STATE open
ENV GH_ISSUE_REACTION +1
# Two more variables included for shake of completeness
# ENV GH_ISSUE_TITLE_MAX_CHARS
# ENV GH_ACCESS_TOKEN

# Run the webserver with 8 workers, listening to any IP
CMD ["gunicorn", "-w", "8", "-b", "0.0.0.0:80", "analytics:app", "gunicorn-scripts"]
