"""
프로그램 설명
"""


def describe():
    """프로그램 설명"""
    print("- 최초 압축해제시도 : 처음으로 압축해제할 때 사용할 수 있습니다.\n")
    print("- 해제되지 않은 압축파일 재시도 : 파일의 갯수가 너무 많아질 경우 압축파일 내 압축파일을 인식하지 못하는 경우가 발생합니다.")
    print("이럴경우, 이를 사용해 최상위 압축파일명 정보를 훼손하지 않고 기존 log 데이터를 사용해 압축해제를 재시도 할 수 있습니다.")
    print("또한, log 데이터가 온전하다는 전제하에 새로운 엑셀 파일로 만드는 것을 권장합니다.\n")
    print("- 로그 파일은 바탕화면에 생성이 됩니다. 오류가 발생할 경우, 쓰기 권한을 확인해주세요.\n")
    print("- 로그 파일은 최상위 압축파일명 정보를 입력하기 위해 꼭 필요합니다.")
    print("압축 해제가 \"완벽하게\" 되었다는 전제 하에 삭제하시기 바랍니다. 로그 파일이 없으면 최상위 압축파일명 데이터는 훼손됩니다")