# Python 이미지 사용
FROM python:3.9-slim

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 파일 복사 및 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 애플리케이션 코드 복사
COPY . .

# 애플리케이션 포트 설정
EXPOSE 8000

# 서버 실행
CMD ["gunicorn", "-b", "0.0.0.0:8000", "your_project.wsgi:application"]