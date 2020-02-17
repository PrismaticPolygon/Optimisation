from zipfile import ZipFile
import os
from shutil import copy

out_path = os.path.join("out", "ffgt86.zip")

zip_obj = ZipFile(out_path, "w")

zip_obj.write("q3.py")
zip_obj.write("q4a.py")
zip_obj.write("q4b.py")
zip_obj.write("q4c.py")

report_path = os.path.join("report", "report.pdf")

copy(report_path, "report.pdf")

zip_obj.write("report.pdf")

os.remove("report.pdf")

zip_obj.close()
