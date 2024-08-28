import os
import subprocess
import pandas as pd
import zipfile

error_files = []


def extract_bandizip(compress_file_path):
    """주어진 압축파일을 Bandizip을 사용하여 압축 해제"""
    try:
        zips_extract_folder = os.path.join('\\\\?\\', os.path.dirname(
            compress_file_path), os.path.splitext(os.path.basename(compress_file_path))[0])
        compress_file_path = os.path.join('\\\\?\\', compress_file_path)
        if not os.path.exists(zips_extract_folder):
            os.makedirs(zips_extract_folder, exist_ok=False)
            subprocess.run(
                ["C:\\Program Files\\Bandizip\\Bandizip.exe", "bx", "-y", "-delsrc",
                 f"-o:{zips_extract_folder}", compress_file_path],
                check=True
            )
        else:
            e_s = "동일 폴더명 존재"
            save_log(compress_file_path, e_s)
            error_files.append(compress_file_path)
            return []
        return [os.path.join(zips_extract_folder, f) for f in os.listdir(zips_extract_folder)]
    except Exception as e:
        save_log(compress_file_path, e)
        error_files.append(compress_file_path)
        return []


def process_folder(folder_path, cnt):
    """지정된 폴더를 순회하면서 압축파일 처리"""
    is_compressed_exists = False
    results = []
    for root, _, files in os.walk(folder_path):
        compress_ext = {'.zip', '.egg', '.7z', '.alz'}
        # .vol2.egg ~ .vol50.egg
        exclude_patterns = {f'.vol{i}.egg' for i in range(2, 51)}
        compress_files = [f for f in files if f.lower().endswith(tuple(compress_ext)) and not any(
            f.lower().endswith(pattern) for pattern in exclude_patterns)]
        exclude_files = [f for f in files if f.lower().endswith(
            tuple(exclude_patterns))]

        for compress_file in compress_files:
            compress_file_path = os.path.join('\\\\?\\', root, compress_file)
            if compress_file_path in error_files:
                continue  # 에러가 발생한 파일 건너뛰기
            if compress_file_path.lower().endswith('.zip'):
                if is_zip_encrypted(compress_file_path):
                    e_e = "암호화된 압축파일"
                    save_log(compress_file_path, e_e)
                    error_files.append(compress_file_path)
                    continue  # 암호화된 압축 파일 건너뛰기
            file_list = extract_bandizip(compress_file_path)
            for file in file_list:
                if file.lower().endswith(tuple(compress_ext)):
                    if is_compressed_exists == False:
                        print("내부 압축파일 발견. 스크립트가 한번 더 진행됩니다.")
                        is_compressed_exists = True
                    results.append(
                        {'File Name': compress_file_path, 'Extracted File': file})

    if exclude_files:
        for rm_file in exclude_files:
            rm_file_path = os.path.join('\\\\?\\', root, rm_file)
            os.remove(rm_file_path)

    df = pd.DataFrame(results)
    df.to_excel(os.path.join('\\\\?\\',
                             folder_path, f'extraction_report({cnt}).xlsx'), index=False)
    print(f"엑셀 파일이 생성되었습니다: extraction_report({cnt}).xlsx")

    return is_compressed_exists


def is_zip_encrypted(zip_path):
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            for zip_info in zip_file.infolist():
                if zip_info.flag_bits & 0x1:
                    return True
            return False
    except Exception as e:
        print(f"[{e}] {zip_path}")
        return False


def save_log(dst, e):
    """로그를 입력폴더 경로 내에 생성"""
    print(f"{e} 압축해제 오류 발생")
    log_dir = os.path.join('\\\\?\\', folder_path, "log.txt")
    with open(log_dir, 'a') as file:
        file.write(f'Error ({e}) , Source File ({dst})\n')


if __name__ == "__main__":
    """내부 압축파일이 있는 경우 모두 해제될 때까지 반복"""
    folder_path = input("폴더 경로를 입력하세요 : ")
    folder_path = os.path.join("\\\\?\\", folder_path)
    cnt = 1
    print(f"압축해제 {cnt}번째 진행 중")
    is_compress_exists = process_folder(folder_path, cnt)
    while is_compress_exists:
        cnt += 1
        print(f"압축해제 {cnt}번째 진행 중")
        is_compress_exists = process_folder(folder_path, cnt)
    print("모든 압축파일 해제가 완료되었습니다")
