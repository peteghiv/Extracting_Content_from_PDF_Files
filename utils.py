import zlib, re, os

def extract_serial_number(path: str) -> str:
    '''
        Extracts the Serial Number from the PDF file.

        Args:
            - path  :   File path to the required PDF file

        Return Vals:
            - SN    :   Serial Number extracted
    '''

    if not os.path.exists(path):
        print(f'Error: File {path} not found.')
        return f'Error: File {path} not found.'
    
    # Read the file in binary format
    with open(path, 'rb') as f:
        pdf = f.read()

    stream = re.compile(b'.*?FlateDecode.*?stream(.*?)endstream', re.S)

    SN = ''

    for s in re.findall(stream, pdf):
        s = s.strip(b'\r\n')

        try:
            temp = zlib.decompress(s).decode('UTF-8')
        
            #   Logic to get the text in the PDF
            #   May need to read character by character and convert hex-dec
            #   In this case, we do not have to due to the result of temp
            if 'Serial Number: ' in temp:
                idx = temp.index("Serial Number: ")     # Use the fixed format of the file to our advantage
                SN = temp[idx+15: idx+30]               # It is guaranteed that the SN is 15 characters long

        except:
            continue

    return SN