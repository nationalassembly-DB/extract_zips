"""
main함수.
내부 압축파일이 존재하지 않을 때까지 반복
"""


import os


from module.process_folder import process_folder


def main():
    """main 함수. 내부 압축파일이 존재하지 않을 때까지 반복"""
    print("-"*24)
    print("\n>>>>>>압축파일 해제<<<<<<\n")
    print("-"*24)
    folder_path = input("폴더 경로를 입력하세요 (종료는 0을 입력, log파일 삭제는 9를 입력) : ")

    if folder_path == '0':
        return 0

    if folder_path == '9':
        os.remove('./log/zip_file.txt')
        print("로그 파일이 정상적으로 삭제되었습니다")
        return main()

    if not os.path.isdir(folder_path):
        print("입력 폴더의 경로를 다시 한번 확인하세요")
        return main()

    folder_path = os.path.join("\\\\?\\", folder_path)
    process_folder(folder_path)

    print("\n~~~모든 압축파일 해제가 완료되었습니다~~~\n")

    return main()


if __name__ == "__main__":
    main()
