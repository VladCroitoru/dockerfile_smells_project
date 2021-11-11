FROM alpine
MAINTAINER David Trudgian

# Create 3 directories, eache containing file1
RUN mkdir -p /test/whiteout-dir /test/whiteout-file /test/normal-dir
RUN touch /test/whiteout-dir/file1 /test/whiteout-file/file1 /test/normal-dir/file1

# Remove opaque-dir, re-create it
RUN rm /test/whiteout-dir/file1
RUN rmdir /test/whiteout-dir
RUN mkdir /test/whiteout-dir

# Put a file 2 in each dir
RUN touch /test/whiteout-dir/file2 /test/whiteout-file/file2 /test/normal-dir/file2

# Remove file1 from the whiteout dir
RUN rm /test/whiteout-file/file1

CMD find /test

