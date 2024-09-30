import os

# good.txt 파일 경로
good_txt_path = '/home/user/바탕화면/Baekjoon/yolo/good_labels.txt'

# 사진들이 있는 폴더 경로
data_split_folder = '/home/user/다운로드/data_split_3 bad 삭제'

# 새로운 텍스트 파일에 겹치는 이름을 저장할 경로
output_file_path = '/home/user/다운로드/matched_good.txt'

# good.txt 파일에서 사진 파일명 읽기
with open(good_txt_path, 'r') as f:
    good_images = set(f.read().splitlines())

# data_split 폴더 내 모든 파일명 가져오기 (하위 폴더 포함)
actual_images = set()
for root, dirs, files in os.walk(data_split_folder):
    for file in files:
        actual_images.add(file)

# 겹치는 파일명 찾기
matched_images = good_images.intersection(actual_images)

# matched_good.txt 파일에 겹치는 파일명 저장
with open(output_file_path, 'w') as f:
    for image in matched_images:
        f.write(image + '\n')

print(f"총 {len(matched_images)}개의 파일명이 겹칩니다. 결과는 {output_file_path}에 저장되었습니다.")
