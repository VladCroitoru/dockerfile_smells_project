FROM docker
ADD inner/* /src/
ENV IMAGE_NAME hello-container
CMD cp -r /installed/* /src && docker build -t $IMAGE_NAME /src
