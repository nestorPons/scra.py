import shutil
import csv

def move_file(folder_download, folder_db, files):
    for l in files:
        print('Moviendo archivo ....')
        shutil.move(folder_download + l , folder_db + l)
        print(folder_download + l + ' => '+ folder_db + l)


def print_csv(folder_db, files):
    print('Scaneando archivo csv....')
    file1 = files[0]
    with open(folder_db + file1, newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            print(row)

def get_title(folder_db, files):
    csv_file = folder_db + files[0]
    print('Imprimiendo cabeceras del archivo ' + csv_file + '...')
    with open(csv_file, 'r') as f:
        reader = csv.reader(f , delimiter=';', quotechar='"')
        cabeceras = next(reader)
        print(cabeceras)
        cabeceras = next(reader)
        print(cabeceras)

def get_dialect(folder_db, files):
    csv_file = folder_db + files[0]
    with open(csv_file) as f:
        dialect = csv.Sniffer().sniff(f.read(1024))
        f.seek(0)
        reader = csv.reader(f, dialect)
        for row in reader:
            print(row)
print(csv.list_dialects())

d=csv.get_dialect('excel')
print("Delimiter: ", d.delimiter)
print("Doublequote: ", d.doublequote)
print("Escapechar: ", d.escapechar)
print("lineterminator: ", repr(d.lineterminator))
print("quotechar: ", d.quotechar)
print("Quoting: ", d.quoting)
print("skipinitialspace: ", d.skipinitialspace)
print("strict: ", d.strict)