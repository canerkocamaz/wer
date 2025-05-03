Here's what the code does:

Scanning Directories:

It walks through all subdirectories inside WER\ReportArchive to find Report.wer files.

Uses os.walk() to traverse the folder structure.

Extracting TargetAppId:

It opens each Report.wer file and reads the lines.

If a line starts with "TargetAppId=", it extracts the value.

Splits the extracted data using "!" to get the SHA-1 hash and file name.

Saving Data to CSV:

It creates wer_reports.csv.

Writes three columns: Directory Path, TargetAppId, SHA-1 Hash.

Every valid Report.wer file entry is recorded into the CSV file.

Logging Progress:

As each file is processed, it prints Kayıt eklendi: {file_path} to track progress.

When all files are processed, it displays "Tamamlandı! CSV dosyası: wer_reports.csv"

Summary
This script automates collecting forensic data from multiple WER\ReportArchive\ folders and stores useful details (TargetAppId, SHA-1 hash) in a structured CSV format. You can use this data for further analysis or forensic investigations.
