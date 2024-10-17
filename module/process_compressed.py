"""
반디집을 사용하여 압축해제를 시도합니다.
암호가 걸린 압축파일은 패스합니다.
"""


import os
import shutil
import subprocess
import zipfile


error_files = {}


def extract_bandizip(compress_file_path):
    """주어진 압축파일을 Bandizip을 사용하여 압축 해제"""
    is_dir_created_by_me = False
    try:
        zips_extract_folder = os.path.join('\\\\?\\', os.path.dirname(
            compress_file_path), os.path.splitext(os.path.basename(compress_file_path))[0])
        compress_file_path = os.path.join('\\\\?\\', compress_file_path)
        if not os.path.exists(zips_extract_folder):
            os.makedirs(zips_extract_folder, exist_ok=False)
            is_dir_created_by_me = True
            subprocess.run(
                ["C:\\Program Files\\Bandizip\\bz.exe", "x", "-y", "-delsrc",
                 f"-o:{zips_extract_folder}", compress_file_path], check=True
            )
            with open('./log/zip_file.txt', 'a', encoding='utf-8') as file:
                file.write(zips_extract_folder + '\n')

        else:
            error_files[compress_file_path] = '복사본'
            _remove_empty_folder(zips_extract_folder, False)
            return [], compress_file_path
        file_list = [os.path.join(zips_extract_folder, f)
                     for f in os.listdir(zips_extract_folder)]

        return file_list
    except Exception:  # pylint: disable=W0703
        error_files[compress_file_path] = '압축파일이상'
        _remove_empty_folder(zips_extract_folder, is_dir_created_by_me)
        return []


def is_zip_encrypted(zip_path):
    """압축파일이 암호화가 되어있는지의 여부 확인"""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            for zip_info in zip_file.infolist():
                if zip_info.flag_bits & 0x1:
                    error_files[zip_path] = '암호화'
                    return True
            return False
    except Exception:  # pylint: disable=W0703
        error_files[zip_path] = '압축파일이상'
        return False


def _remove_empty_folder(folder_path, is_dir_created_by_me):
    """폴더 생성후 압축 시도시 exception이 발생시 폴더를 삭제합니다"""
    try:
        if os.path.exists(folder_path) and not os.listdir(folder_path):
            os.rmdir(folder_path)
        if os.path.exists(folder_path) and is_dir_created_by_me:
            shutil.rmtree(folder_path)
    except Exception:  # pylint: disable=W0703
        error_files[folder_path] = '폴더이상(확인필수)'
