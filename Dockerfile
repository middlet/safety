#
# Dockerfile for django application
#

FROM ubuntu:12.10

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get upgrade -y


RUN apt-get install -y git-core python-pip
RUN apt-get install -y firefox xvfb
