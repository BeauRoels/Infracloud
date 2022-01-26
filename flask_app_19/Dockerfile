FROM python:latest
RUN pip install flask && pip install datetime
COPY ./static /home/mc/static/
COPY ./templates /home/mc/templates/
COPY ./flask_app.py /home/mc/
EXPOSE 5555
CMD python /home/mc/flask_app.py

