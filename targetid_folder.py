import os
import csv

def extract_target_app_id(file_path):
    """Report.wer dosyasindan TargetAppId satirini okuyup SHA-1 hash ve dosya adini çikarir."""
    try:
        with open(file_path, "r", encoding="utf-16") as f:
            for line in f:
                if "TargetAppId=" in line:
                    target_app_id = line.strip().replace("\r", "").replace("\n", "").replace(" ", "")
                    target_app_id = target_app_id.split("=", 1)[1]
                    
                    # "!" işaretine göre parçala
                    parçalar = target_app_id.split("!")
                    if len(parçalar) >= 3:
                        sha1_hash = parçalar[-2]  # SHA-1 hash değeri
                        filename = parçalar[-1]  # Dosya adi
                        return target_app_id, sha1_hash
    except Exception as e:
        print(f"Hata: {e}")

    return None, None

def process_wer_files(base_dir, output_csv):
    """WER klasör yapisini tarar ve Report.wer dosyalarini analiz edip CSV'ye kaydeder."""
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Dizin Yolu", "TargetAppId", "SHA-1 Hash"])

        for root, _, files in os.walk(base_dir):
            for file in files:
                if file.lower() == "report.wer":
                    file_path = os.path.join(root, file)
                    target_app_id, sha1_hash = extract_target_app_id(file_path)

                    if target_app_id and sha1_hash:
                        writer.writerow([file_path, target_app_id, sha1_hash])
                        print(f"Kayit eklendi: {file_path}")
                    
    print(f"\nTamamlandi! CSV dosyasi: {output_csv}")

# Kullanim
base_directory = r"WER\ReportArchive"  # Klasör yapisinin ana dizini
output_file = "wer_reports.csv"  # Çikti CSV dosyasi
process_wer_files(base_directory, output_file)
