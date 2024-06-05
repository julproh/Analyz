import csv

def csv_to_html(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        data = list(reader)

    html = "<table>\n"
    for row in data:
        html += "  <tr>\n"
        for cell in row:
            html += f"    <td>{cell}</td>\n"
        html += "  </tr>\n"
    html += "</table>"

    return html

csv_file = 'dog_breeds.csv'
html_table = csv_to_html(csv_file)
print(html_table)