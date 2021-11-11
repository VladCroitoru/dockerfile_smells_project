FROM python:3.6

# Create a virtualenv for the application dependencies.
RUN pip install --no-cache-dir \
	virtualenv

RUN virtualenv -p python3 /env

# Set virtualenv environment variables. This is equivalent to running
# source /env/bin/activate. This ensures the application is executed within
# the context of the virtualenv and will have access to its dependencies.
ENV VIRTUAL_ENV /env
ENV PATH /env/bin:$PATH

# Install dependencies.
ADD requirements.txt /src/requirements.txt
RUN pip install -r /src/requirements.txt

# Add application code.
ADD . /src

EXPOSE 8000
WORKDIR /src/opsdash
CMD gunicorn -b :8000 opsdash.wsgi:application



