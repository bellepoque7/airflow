# 모든 dag 에 필요한 부분
from __future__ import annotations

import datetime

import pendulum #datetime을 쉽게 관리하는 모듈듈

from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator 


with DAG(
    dag_id="dags_bash_operator",  #처음 보이는 dag 이름, 파이썬 파일명과 무관하나 일치시키는게 좋음
    schedule="0 0 * * *",         #cron 양식의 실행 주기 (분,시,일,월,요일)
    start_date=pendulum.datetime(2021, 1, 1, tz="Asia/Seoul"), #시작 시간, UTC: 세계 표준시, 한국시간으로 변경
    catchup=False,               #False: 사이 누락된 구간 돌리지않음, True: 누락된 기간 "한꺼번"에 돌림, 일반적으로는 False 설정
    dagrun_timeout=datetime.timedelta(minutes=60), 
    tags=["example", "example2"],  #기억하기 쉬운 태그 옵션
    #params={"example_key": "example_value"}, #태스크에 콩동적으로넘겨줄 파라미터
) as dag:
    bash_t1 = BashOperator(     # Task 객체명
    task_id="bash_t1",          # graph 탭에 나오는 Task 이름, 객체명과 동일하게 설정궈낭
    bash_command="echo whoami", #
    ),
    bash_t2 = BashOperator(
        task_id = "bash_t2"
        bash_command = "echo $HOSTNAME" # 환경변수 HOSTNAME 출력하기
    )
    bash_t1 >> bash_t2  # Task 실행 순서