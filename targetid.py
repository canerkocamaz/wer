def extract_target_app_id(file_path):
    try:
        with open(file_path, "r", encoding="utf-16") as f:
            for line in f:
                if "TargetAppId=" in line:
                    target_app_id = line.strip().replace("\r", "").replace("\n", "").replace(" ", "")
                    target_app_id = target_app_id.split("=", 1)[1]  # "TargetAppId=" kısmını kaldırıyoruz
                    print(f"Temizlenmiş TargetAppId değeri: {repr(target_app_id)}")

                    # "!" işaretine göre parçala
                    parçalar = target_app_id.split("!")
                    
                    if len(parçalar) >= 3:
                        sha1_hash = parçalar[-2]  # SHA-1 hash değeri
                        filename = parçalar[-1]  # Dosya adı
                        return sha1_hash, filename
    except Exception as e:
        print(f"Hata: {e}")

    return None, None

# Kullanım
file_path = "Report.wer"
sha1_hash, filename = extract_target_app_id(file_path)

if sha1_hash and filename:
    print(f"SHA-1 Hash: {sha1_hash}")
    print(f"Dosya Adı: {filename}")
else:
    print("TargetAppId satırı parse edilemedi.")
