"""
main함수.
내부 압축파일이 존재하지 않을 때까지 반복
"""


import os


from module.log import get_log_path
from module.process_folder import process_folder


def main():
    """main 함수. 내부 압축파일이 존재하지 않을 때까지 반복"""
    print("-"*24)
    print("\n>>>>>>압축파일 해제<<<<<<\n")
    print("-"*24)
    select_input = input("1. 최초 압축해제시도 2. 해제되지 않은 압축파일 재시도 : ")

    folder_path = input(
        "폴더 경로를 입력하세요 (종료는 0을 입력, log파일 삭제는 9를 입력)\n(위원회별로 log를 삭제하는 것을 권장합니다) : ")

    if folder_path == '0':
        return 0

    if folder_path == '9':
        if os.path.exists(get_log_path()):
            os.remove(get_log_path())
            print("로그 파일이 정상적으로 삭제되었습니다")
        else:
            print("로그 파일이 존재하지 않습니다.")
        return main()

    if not os.path.isdir(folder_path):
        print("입력 폴더의 경로를 다시 한번 확인하세요")
        return main()

    excel_path = input("엑셀 파일 경로를 입력하세요 (확장자 포함) : ")

    folder_path = os.path.join("\\\\?\\", folder_path)

    if select_input == '1':
        process_folder(folder_path, excel_path, 1)
    elif select_input == '2':
        process_folder(folder_path, excel_path, 90)
    else:
        print('잘못 입력하셨습니다. 다시 시도하세요')

        return main()

    print("\n~~~모든 압축파일 해제가 완료되었습니다~~~\n")

    return main()


if __name__ == "__main__":
    main()
