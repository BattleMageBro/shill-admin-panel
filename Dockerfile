FROM python:3.9
# set work directory
RUN mkdir -p /admin_panel/
WORKDIR /admin_panel/
# copy project
COPY . /admin_panel/
# install dependencies
RUN pip install -r requirements.txt
