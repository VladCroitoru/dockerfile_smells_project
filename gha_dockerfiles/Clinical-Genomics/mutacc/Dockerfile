FROM frolvlad/alpine-miniconda3

# Install picard using conda
RUN conda update -n base -c defaults conda && conda install -c bioconda picard

# Install required libs
RUN apk update \
	&& apk --no-cache add gcc bash python3 libc-dev zlib-dev

# Copy Mutacc to the image
WORKDIR /home/worker/app
COPY . /home/worker/app

# Run commands as non-root user
RUN adduser -D worker

# Grant non-root user permissions over the working directory
RUN chown worker:worker -R /home/worker

# Install Mutacc
RUN pip install mutacc

USER worker
