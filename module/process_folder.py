"""
폴더를 순회하며 압축파일을 압축해제합니다.
압축해제를 완료한후, 다시 폴더를 순회하며 엑셀로 파일리스트를 작성합니다.
압축파일을 해제하며 암호화된 파일, 오류가 있는 파일을 분류합니다.
:param folder_path: 순회할 폴더의 최상위 경로
:return is_compressed_exists: 내부 압축파일이 존재하는지의 여부
"""


from module.compress import *


import os


def process_folder(folder_path):
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
