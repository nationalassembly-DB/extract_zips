"""
폴더를 순회하며 압축파일을 압축해제합니다.
압축해제를 완료한후, 다시 폴더를 순회하며 엑셀로 파일리스트를 작성합니다.
압축파일을 해제하며 암호화된 파일, 오류가 있는 파일을 분류합니다.
:param folder_path: 순회할 폴더의 최상위 경로
:return is_compressed_exists: 내부 압축파일이 존재하는지의 여부
"""


import os


from module.process_compressed import extract_bandizip, is_zip_encrypted, error_files
from module.create_metadata import create_metadata


compress_ext = {'.zip', '.egg', '.7z', '.alz'}


def process_folder(folder_path, try_nums=1):  # pylint: disable=R0912
    """지정된 폴더를 순회하면서 압축파일 처리"""
    is_compressed_exists = False
    for root, _, files in os.walk(folder_path):
        # .vol2.egg ~ .vol50.egg
        exclude_patterns = {f'.vol{i}.egg' for i in range(2, 51)}
        compress_file_path = [os.path.join('\\\\?\\', root, f) for f in files if f.lower().endswith(
            tuple(compress_ext)) and not any(f.lower().endswith(pattern)
                                             for pattern in exclude_patterns)]
        exclude_files_path = [os.path.join('\\\\?\\', root, f) for f in files if f.lower().endswith(
            tuple(exclude_patterns))]

        for compress_file in compress_file_path:
            if compress_file in error_files:
                continue  # 에러가 발생한 파일 건너뛰기
            if compress_file.lower().endswith('.zip') and is_zip_encrypted(compress_file):
                continue  # 암호화된 압축 파일 건너뛰기

            is_compressed_exists = extract_bandizip(
                compress_file, try_nums, folder_path)

    if exclude_files_path:
        for rm_file in exclude_files_path:
            os.remove(rm_file)

    if not is_compressed_exists:
        print("\n======파일리스트를 생성합니다======\n")
        create_metadata(folder_path)
    else:
        try_nums += 1
        print(f"\n======({try_nums}번째) 스크립트를 다시 실행합니다======\n")
        process_folder(folder_path, try_nums)
