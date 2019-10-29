FROM python:3.7-slim
WORKDIR /web_app
COPY ./pycharmprojects/untitled1/web_app /web_app
RUN pip install --trusted-host pypi.python.orh -r requirements.txt
EXPOSE 80
CMD ["python", "LibreApp.py"]
