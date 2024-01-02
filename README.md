# README

This repository contains two files and related scripts: `balance_line.py` and `fileorderer.py`.

## balance_line.py

### Description
The `balance_line.py` script reads two files, `file1.txt` and `file2.txt`, which are sorted alphabetically line by line. Subsequently, the script creates a third file, `file3.txt`, containing the sum of the two input files while maintaining alphabetical order. The adopted approach ensures that operations are performed line by line, without the need to read both files entirely into memory, making it efficient even for large-sized files.

### Features
1. Reading of `file1.txt` and `file2.txt` alphabetically line by line.
2. Generation of `file3.txt` containing the sum of the two files while maintaining alphabetical order.
3. Efficient approach, reading line by line to optimize memory usage.

### Usage
```bash
python balance_line.py
```

## fileorderer.py

### Description
The `fileorderer.py` script aims to sort a file alphabetically. Using the Iterable sort concept, the script iterates through the file and organizes all records in alphabetical order.

### Features
1. Sorting of records in a file alphabetically.
2. Implementation of the Iterable sort concept for efficiency in the process.

### Usage
```bash
python fileorderer.py file_name.txt
```

**Note:** Replace "file_name.txt" with the name of the file you want to sort.

---

Feel free to explore the scripts and adapt them as needed to meet your specific requirements.