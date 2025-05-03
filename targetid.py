def extract_target_app_id(file_path):
    try:
        with open(file_path, "r", encoding="utf-16") as f:
            for line in f:
                if "TargetAppId=" in line:
                    target_app_id = line.strip().replace("\r", "").replace("\n", "").replace(" ", "")
                    target_app_id = target_app_id.split("=", 1)[1]  # remove "TargetAppId="
                    print(f"cleaned TargetAppId value: {repr(target_app_id)}")

                    # parse by "!" sign
                    parts = target_app_id.split("!")
                    
                    if len(parts) >= 3:
                        sha1_hash = parts[-2]  # SHA-1 hash value
                        filename = parts[-1]  # File name
                        return sha1_hash, filename
    except Exception as e:
        print(f"Error: {e}")

    return None, None

# Usage
file_path = "Report.wer"
sha1_hash, filename = extract_target_app_id(file_path)

if sha1_hash and filename:
    print(f"SHA-1 Hash: {sha1_hash}")
    print(f"File Name: {filename}")
else:
    print("TargetAppId couldn't parsed..")
