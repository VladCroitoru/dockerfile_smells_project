FROM ipython/ipython

# Provided as an example, should be used as part of an image that creates a user

ADD kernels.py /srv/

# The exec form causes kernels to restart unless invoked with sh -c
CMD ["sh", "-c", "/srv/kernels.py"]
