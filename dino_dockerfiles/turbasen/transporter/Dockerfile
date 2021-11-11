FROM quay.io/compose/transporter:v0.2.0

# Create a directory where the application code should live and set it as the
# current working directory
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Copy the application source code
COPY . /usr/src/app

ENTRYPOINT ["/bin/sh", "-c"]

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]
