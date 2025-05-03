import os
import csv

def extract_target_app_id(file_path):
    """Reads Report.wer file and extracts SHA-1 value and file name from TargetAppId line"""
    try:
        with open(file_path, "r", encoding="utf-16") as f:
            for line in f:
                if "TargetAppId=" in line:
                    target_app_id = line.strip().replace("\r", "").replace("\n", "").replace(" ", "")
                    target_app_id = target_app_id.split("=", 1)[1]
                    
                    # parse by "!" sign
                    parts = target_app_id.split("!")
                    if len(parts) >= 3:
                        sha1_hash = parts[-2]  # SHA-1 hash value
                        filename = parts[-1]  # File name
                        return target_app_id, sha1_hash
    except Exception as e:
        print(f"Error: {e}")

    return None, None

def process_wer_files(base_dir, output_csv):
    """scan WER folder, analyse Report.wer files then save results to a CSV file ."""
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Folder Path Yolu", "TargetAppId", "SHA-1 Hash"])

        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.lower() == "report.wer":
                    file_path = os.path.join(root, file)
                    target_app_id, sha1_hash = extract_target_app_id(file_path)

                    if target_app_id and sha1_hash:
                        writer.writerow([file_path, target_app_id, sha1_hash])
                        print(f"Record added: {file_path}")
                    
    print(f"\Completed! CSV file: {output_csv}")

# Usage
base_directory = r"WER\ReportArchive"  # base folder
output_file = "wer_reports.csv"  # CSV file
process_wer_files(base_directory, output_file)
