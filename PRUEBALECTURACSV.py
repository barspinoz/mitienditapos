import csv

# Read CSV file
def read_csv(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                print(row)
    except FileNotFoundError:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    # Specify your CSV file path
    csv_file = "productos.csv"
    read_csv(csv_file)