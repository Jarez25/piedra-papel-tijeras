import csv


my_csv = open("intermedio/my_csv.csv", "w+")

csv_writer =  csv.writer(my_csv)
csv_writer.writerow(['nombre', 'apellido', 'edad', 'lenguaje'])
csv_writer.writerow(['jairo', 'medina',25, 'python' ])
csv_writer.writerow(['jairo', 'medina',25, 'python' ])
csv_writer.writerow(['jairo', 'medina',25, 'python' ])
