FROM centos:centos7
MAINTAINER rtx3 <r@rtx3.com>>

RUN yum -y install epel-release
RUN yum -y install python-devel python-pip python-setuptools git
RUN yum -y update

RUN cd /opt && \
    git clone https://github.com/pstocky/pstocky.git

RUN cd /opt/pstocky && \
    pip install -r backend/requirements.txt

RUN chmod 777 /opt/pstocky/backend/settings.py

ADD ./local_settings.docker /opt/pstocky/backend/settings.py

EXPOSE 8000
WORKDIR /opt/pstocky

CMD ["/usr/bin/python","/opt/pstocky/backend/run.py"]
