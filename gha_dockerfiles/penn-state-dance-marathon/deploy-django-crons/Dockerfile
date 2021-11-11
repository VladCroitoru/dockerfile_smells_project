FROM thontechnology/amazonlinux2-python:3.8

# Install AWS CLI for S3 upload
RUN yum install -y unzip \
    && curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" \
    && unzip awscliv2.zip \
    && ./aws/install

# Install boto3 to run the Python script
RUN pip install boto3

COPY update_lambda_code.py /update_lambda_code.py
COPY collectstatic_and_migrate.py /collectstatic_and_migrate.py
COPY build_lambda.sh /build_lambda.sh
RUN chmod +x /build_lambda.sh

ENTRYPOINT ["/build_lambda.sh"]
