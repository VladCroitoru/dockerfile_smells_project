FROM ozanzal/gophernotes

RUN apt-get install -y nodejs-legacy npm libzmq3-dev && \
    npm install -g ijavascript

ADD ./js_kernel.json /root/.local/share/jupyter/kernels/javascript/kernel.json
RUN cp /usr/local/lib/node_modules/ijavascript/images/logo-32x32.png /root/.local/share/jupyter/kernels/javascript/
RUN cp /usr/local/lib/node_modules/ijavascript/images/logo-64x64.png /root/.local/share/jupyter/kernels/javascript/

EXPOSE 8888
ENTRYPOINT ["tini", "--"]
CMD ["jupyter", "notebook"]
