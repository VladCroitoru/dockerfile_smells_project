FROM cityofla/ita-data-civis-lab:sha-4888c7e  
RUN curl -sSL https://sdk.cloud.google.com |bash
ENV PATH="/root/google-cloud-sdk/bin:${PATH}"
RUN apt-get update --allow-releaseinfo-change && apt-get install -y \
  golang
WORKDIR /app
COPY ./ ./
#RUN go build for Google Cloud Run web trigger
RUN go build -v -o server
COPY conda-requirements.txt /tmp/
RUN conda install --yes -c conda-forge --file /tmp/conda-requirements.txt
COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt
RUN python setup.py install
#CMD to start Google Cloud Run server for web trigger
CMD ["/app/server"]
