from datetime import date
import os


today = date.today()
error_count = 0
total_line = 0
file_path  = "C:\\Users\\Tharuka\\Desktop\\Python\\projects\\log Parser\\sample-100kb.log"
file_name = os.path.basename(file_path)

with open('sample-100kb.log', 'r') as file:
    for line in file:
        total_line += 1
        if "ERROR" in line:
             error_count += 1 
    

print("--------📊 System Log Analysis Report---------")
print(f"Report Generated Date: {today}")
print(f"Log File Name: {file_name}")
print(f"Total Lines Processed: {total_line}")
print(f"Total Errors Found: {error_count}")