import os, csv
from utils import extract_serial_number

RESULTS_FILE = 'results.csv'
cwd = os.getcwd()
E_TIX_DIR = os.path.join(cwd, 'E-Tickets')

# Create the results file if it does not exist yet
if not os.path.exists(RESULTS_FILE):
    print('Creating CSV file...')
    with open(RESULTS_FILE, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Filename', 'Serial Number'])

def main() -> None:
    # Get the files which we need to process
    filenames = [filename for filename in os.listdir(E_TIX_DIR) if filename.endswith('.pdf')]

    for filename in filenames:
        SN = extract_serial_number(os.path.join(E_TIX_DIR, filename))

        # Check for invalid serial numbers
        if 'Error' in SN or SN == '':
            continue

        # Add the valid serial number to the CSV file
        with open(RESULTS_FILE, 'a', newline='') as f:
            writer = csv.writer(f)

            writer.writerow([
                filename,
                SN
            ])

if __name__ == '__main__':
    main()
    print('Done')