"""로그를 관리하는 파일입니다"""
import os
import sys


def get_log_path():
    """패키지, 스크립트에 따른 다른 log PATH를 반환합니다"""
    if hasattr(sys, 'frozen'):
        tmp_path = os.path.expanduser('~')
        os.makedirs(f'{tmp_path}\\Desktop\\log_zips', exist_ok=True)
        return f'{tmp_path}\\Desktop\\log_zips\\zip_file.txt'
    os.makedirs('./log', exist_ok=True)
    return './log/zip_file.txt'


def remove_log():
    """로그 파일을 삭제합니다"""
    if os.path.exists(get_log_path()):
        os.remove(get_log_path())
        print("로그 파일이 정상적으로 삭제되었습니다")
    else:
        print("로그 파일이 존재하지 않습니다.")
