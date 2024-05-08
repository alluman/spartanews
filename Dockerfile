# python
FROM python:3.10.11

# 디렉토리
WORKDIR /spartanews

# pip install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 포트
EXPOSE 8000

# 서버 실행
CMD ["gunicorn", "-b", "0.0.0.0:8000", "spartanews.wsgi:application"]