FROM osgeo/gdal:ubuntu-full-3.3.1

RUN \
  apt -y update --fix-missing && \
  apt -y install software-properties-common && \
  apt -y update && \
  apt -y upgrade && \
  apt -y install python3-pip && \
  rm -rf /var/lib/apt/lists/*

COPY src/requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . ./

#COPY src/entry_script.sh /entry_script.sh
ADD src/aws-lambda-rie /usr/local/bin/aws-lambda-rie
ENTRYPOINT [ "src/entry_script.sh" ]

#WORKDIR /workspace
#COPY . /workspace
CMD [ "src/lambda_function.lambda_handler" ]
