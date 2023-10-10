import requests
import os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import sqlite3
import time

class UpdatingEventHandler(PatternMatchingEventHandler):
    def __init__(self):
        super(UpdatingEventHandler, self).__init__(patterns=["./images/*.jpg"])
	
    def on_created(self, event):
        super(UpdatingEventHandler, self).on_created(event)

        # images 폴더내에 파일이 created 됐을 때 호출되는 함수
        file_path = event.src_path
        filename = file_path.split("/")[-1]

        # filename 은 <patient_id>_<exam_date>_<R or L>.jpg 로 구성되어 있다고 가정한다.
        # filename 을 파싱하여 patient_id, exam_date, laterality(좌,우) 을 찾는다.

        patient_id = ""
        exam_date = ""
        laterality = ""

        #################

        
        # 파싱한 위 정보를 sqlite 데이터베이스에 저장하는 query 를 작성, schema 는 init.sql 파일 참고
        conn = sqlite3.connect("image.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO .... ")

        # requests 패키지를 사용하여 이미지 파일과 파일정보를 API 를 이용해 업로드 한다. API 사용방법은 README 파일 참고

        data = {
            #.....
        } 

        res = requests.post("https://test.mediwhale.net/local_uploader/upload")

        # status 가 200 인 경우 success 를 출력한다.
        if res.status == 200 :
            print("success")



if __name__ == "__main__":
    event_handler = UpdatingEventHandler()
    observer = Observer()
    observer.schedule(event_handler, "./images", recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()




