from extract_compressed_file import folder_path


import os


def save_log(dst, e):
    """로그를 입력폴더 경로 내에 생성"""
    print(f"{e} 압축해제 오류 발생")
    log_dir = os.path.join('\\\\?\\', folder_path, "log.txt")
    with open(log_dir, 'a') as file:
        file.write(f'Error ({e}) , Source File ({dst})\n')
