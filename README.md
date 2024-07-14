# Extracting Content from PDF Files

This repository contains simple code to extract Serial Numbers from PDF Files.

It does not require any external modules, and only uses `zlib` and `re`.

It is guaranteed that all of the PDF Files in the sub-folder `E-Tickets` have the same format, and each serial number is a _randomised 15-digit string_.

## Methodology
1. Read the PDF File in Binary Mode.
2. Use `re` to find FlateDecode objects in the PDF document.
3. Use `zlib` to unzip these objects.
4. Use simple logic to identify the serial number.

## Credits
Utilises code from https://gist.github.com/averagesecurityguy/ba8d9ed3c59c1deffbd1390dafa5a3c2 
