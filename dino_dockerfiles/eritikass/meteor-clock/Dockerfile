FROM ulexus/meteor

# before making the image, exec
# meteor build --directory meteor_build

COPY meteor_build /home/meteor/www
RUN chown -R meteor:meteor /home/meteor/