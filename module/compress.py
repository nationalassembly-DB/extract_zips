"""
반디집을 사용하여 압축해제를 시도합니다.
암호가 걸린 압축파일은 패스합니다.
"""


import os
import subprocess
import zipfile
from zipfile import BadZipFile

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
            error_files.append(compress_file_path)
            return []
        return [os.path.join(zips_extract_folder, f) for f in os.listdir(zips_extract_folder)]
    except FileNotFoundError:
        error_files.append(compress_file_path)
        return []
    except Exception:
        error_files.append(compress_file_path)
        return []


def is_zip_encrypted(zip_path):
    """압축파일이 암호화가 되어있는지의 여부 확인"""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_file:
            for zip_info in zip_file.infolist():
                if zip_info.flag_bits & 0x1:
                    error_files.append(zip_path)
                    return True
            return False
    except BadZipFile:
        error_files.append(zip_path)
        return False
    except Exception:
        error_files.append(zip_path)
        return False
