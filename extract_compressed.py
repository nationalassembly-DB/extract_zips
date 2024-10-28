"""
main함수.
내부 압축파일이 존재하지 않을 때까지 반복
"""


import os


from module.create_metadata import create_metadata
from module.describe_script import describe
from module.log import remove_log
from module.process_folder import process_folder


def main():
    """main 함수. 내부 압축파일이 존재하지 않을 때까지 반복"""
    print("-"*24)
    print("\n>>>>>>압축파일 해제<<<<<<\n")
    print("-"*24)
    select_input = input(
        "1. 최초 압축해제시도, 2. 해제되지 않은 압축파일 재시도, 3. 파일리스트만 작성, 5. 프로그램 설명, 9. log삭제, 0. 종료: ")

    if select_input == '0':
        return 0

    if select_input == '5':
        describe()
        return main()

    if select_input == '9':
        remove_log()
        return main()

    folder_path = input(
        "폴더 경로를 입력하세요 : ")

    if not os.path.isdir(folder_path):
        print("입력 폴더의 경로를 다시 한번 확인하세요")
        return main()

    excel_path = input("엑셀 파일 경로를 입력하세요 (확장자 포함) : ")

    folder_path = os.path.join("\\\\?\\", folder_path)

    if select_input == '1':
        process_folder(folder_path, excel_path, 1)
    elif select_input == '2':
        process_folder(folder_path, excel_path, 90)
    elif select_input == '3':
        create_metadata(folder_path, excel_path)
    else:
        print('잘못 입력하셨습니다. 다시 시도하세요')
        return main()

    print("\n~~~모든 압축파일 해제가 완료되었습니다~~~\n")

    return main()


if __name__ == "__main__":
    main()
