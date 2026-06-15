import re, csv

output_file = open('error_report.csv', 'w', newline='')
output_writer = csv.writer(output_file)

with open("../task1/sample.log", "r") as log:
    for line in log:
        errors = re.findall(r"\[(\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] ERROR (\w+): (.+)", line)
        for error in errors:
            date, error_type, message = error
            output_writer.writerow([date, error_type, message])
output_file.close()