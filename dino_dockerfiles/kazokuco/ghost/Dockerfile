FROM ghost:0.11.0
RUN npm install -q --no-color ghost-storage-adapter-s3 pg && npm cache clean
RUN mkdir content/storage && cp -r node_modules/ghost-storage-adapter-s3 content/storage/s3
RUN chown -R user .
ADD config.js config.js

# Reset Ghost's entrypoint nonsense >_>
ENTRYPOINT []
CMD ["bash", "-c", "npm start || cat npm-debug.log"]
