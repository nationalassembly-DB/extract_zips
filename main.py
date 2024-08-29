import os

from module.process_folder import process_folder

if __name__ == "__main__":
    """내부 압축파일이 있는 경우 모두 해제될 때까지 반복"""
    folder_path = input("폴더 경로를 입력하세요 : ")
    folder_path = os.path.join("\\\\?\\", folder_path)
    cnt = 1
    print(f"압축해제 {cnt}번째 진행 중")
    IS_COMPRESS_EXISTS = process_folder(folder_path)
    while IS_COMPRESS_EXISTS:
        cnt += 1
        print(f"압축해제 {cnt}번째 진행 중")
        IS_COMPRESS_EXISTS = process_folder(folder_path)
    print("모든 압축파일 해제가 완료되었습니다")
