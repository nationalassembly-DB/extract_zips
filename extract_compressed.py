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
    select_input = input(
        "1. 최초 압축해제시도, 2. 해제되지 않은 압축파일 재시도, 5. 프로그램 설명, 9. log삭제, 0. 종료: ")

    if select_input == '0':
        return 0

    if select_input == '5':
        print("- 최초 압축해제시도 : 처음으로 압축해제할 때 사용할 수 있습니다.")
        print("- 해제되지 않은 압축파일 재시도 : 파일의 갯수가 너무 많아질 경우 압축파일 내 압축파일을 인식하지 못하는 경우가 발생합니다.")
        print("이럴경우, 이를 사용해 최상위 압축파일명 정보를 훼손하지 않고 기존 log 데이터를 사용해 압축해제를 재시도 할 수 있습니다.")
        print("- 로그 파일은 프로그램이 위치하는 디렉토리에 생성이 됩니다. 오류가 발생할 경우, 쓰기 권한을 확인하거나 프로그램 위치를 옮기세요")
        print("로그 파일은 최상위 압축파일명 정보를 입력하기 위해 꼭 필요합니다.")
        print("압축 해제가 \"완벽하게\" 되었다는 전제 하에 삭제하시기 바랍니다. 로그 파일이 없으면 최상위 압축파일명 데이터는 훼손됩니다")

        return main()

    if select_input == '9':
        if os.path.exists(get_log_path()):
            os.remove(get_log_path())
            print("로그 파일이 정상적으로 삭제되었습니다")
        else:
            print("로그 파일이 존재하지 않습니다.")
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
    else:
        print('잘못 입력하셨습니다. 다시 시도하세요')

        return main()

    print("\n~~~모든 압축파일 해제가 완료되었습니다~~~\n")

    return main()


if __name__ == "__main__":
    main()
