"""로그를 관리하는 파일입니다"""
import os
import sys


def get_log_path():
    """패키지, 스크립트에 따른 다른 log PATH를 반환합니다"""
    if hasattr(sys, 'frozen'):
        tmp_path = os.path.expanduser('~')
        os.makedirs(f'{tmp_path}\\Desktop\\log_zips', exist_ok=True)
        return f'{tmp_path}\\Desktop\\log_zips\\zip_file.txt'  # pylint: disable=W0212
    os.makedirs('./log', exist_ok=True)
    return './log/zip_file.txt'
