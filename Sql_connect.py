import sqlite3

db = sqlite3.connect("Modified_pixel_content.db")
cr = db.cursor()
cr.execute("create table GM_TH_WT_CCED_CORNER_EDGES_VALUES_WANG"
           "(IMAGE_NAME text,Gradient text,Tophat text,"
           "Blackhat text)")
db.commit()
db.close()
print("Softwaves..")
