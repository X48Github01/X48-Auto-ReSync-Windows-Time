# X48-Auto-ReSync-Windows-Time
## == How To ==
    วิธีใช้งาน (Python)
        1.) เปิด CMD โดย Run As Admin เพื่อให้สิทธิการเข้าถึง Services.msc ของ Windows
        2.) Path ที่อยู่ของ Files Python
        3.) ใช้คำสั่งดังต่อไปนี้
            3.1) python autosynctime.py
            3.2) Enter
        4.) พิมพ์เวลาที่ต้องการให้โปรแกรมทำงานทุกๆ กี่นาที/ชั่วโมง โดยจะมีหน่วยเป็น  >> วินาที <<
            60 = 1 minute
            900 = 15 minute
            1800 = 30 minute
            3600 = 1 hour
            14400 = 4 hour
            21600 = 6 hour
            43200 = 12 hour

## == แปลงไฟล์เป็น .exe เพื่อง่ายต่อการใช้งาน ==
    pip install pyinstaller
    pip install colorama
    pip install Console

    ===========================================================
    หลังจาก pip install ครบ ให้ทำตามขั้นตอนดังต่อไปนี้
    1. เปิดไฟล์ CMD ขึ้นมา แล้ว Path ที่อยู่ของไฟล์ให้ถูกต้อง
    2. ใช้คำสั่งดังต่อไปนี้
        2.1 pyinstaller --onefile --clean autosynctime.py
    3. หลังจาก Compile File To EXE เสร็จสิ้น ไฟล์จะอยู่ใน Folder ที่ชื่อว่า dict
    4. เปิดโปรแกรมโดยการคลิกขวา Run As Admin
    5. พิมพ์เวลาที่ต้องการให้โปรแกรมทำงานทุกๆ กี่นาที/ชั่วโมง โดยจะมีหน่วยเป็น  >> วินาที <<

            60 = 1 minute
            900 = 15 minute
            1800 = 30 minute
            3600 = 1 hour
            14400 = 4 hour
            21600 = 6 hour
            43200 = 12 hour
