FROM awalach/raspbian_lite:jessie_python
EXPOSE 80
WORKDIR /opt/face
ADD ./src /opt/face/
