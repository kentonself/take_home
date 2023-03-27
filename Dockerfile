FROM python:3.10-slim

WORKDIR /home/sauce

RUN pip install pytest selenium Appium-Python-Client 

COPY sauce_py_test.py .

CMD ["pytest"]
