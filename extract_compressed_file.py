import os
import pandas as pd

from module.compress import extract_bandizip, is_zip_encrypted, error_files


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
                    continue  # 암호화된 압축 파일 건너뛰기
            file_list = extract_bandizip(compress_file_path)
            for file in file_list:
                if file.lower().endswith(tuple(compress_ext)):
                    if is_compressed_exists == False:
                        print("내부 압축파일 발견. 스크립트가 한번 더 진행됩니다.")
                        is_compressed_exists = True

    if exclude_files:
        for rm_file in exclude_files:
            rm_file_path = os.path.join('\\\\?\\', root, rm_file)
            os.remove(rm_file_path)

    return is_compressed_exists


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
