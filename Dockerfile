from amazonlinux:latest

RUN curl --silent --location https://rpm.nodesource.com/setup_8.x | bash -
RUN yum -y install nodejs

RUN amazon-linux-extras install python3

RUN yum -y install java-1.8.0-openjdk-devel

RUN mkdir /tmp/work/

ADD questions /tmp/work/questions
ADD checker.py /tmp/work/