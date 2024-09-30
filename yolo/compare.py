import os

# 파일 경로
all_name_txt_path = '/home/user/바탕화면/Baekjoon/yolo/all_name.txt'
red_traffic_lights_txt_path = '/home/user/바탕화면/Baekjoon/yolo/red_traffic_lights.txt'
output_txt_path = '/home/user/바탕화면/Baekjoon/yolo/bad_traffic_lights.txt'

# 파일에서 이미지 파일명을 읽어오기
def read_file(file_path):
    with open(file_path, 'r') as f:
        return set(f.read().splitlines())

# 파일명 읽어오기
all_images = read_file(all_name_txt_path)
red_traffic_lights_images = read_file(red_traffic_lights_txt_path)

# all_name.txt에만 있고 red_traffic_lights.txt에 없는 파일
bad_traffic_images = all_images - red_traffic_lights_images

# bad_traffic_lights.txt 파일에 저장하기
with open(output_txt_path, 'w') as f:
    for image in bad_traffic_images:
        f.write(image + '\n')

print(f"{len(bad_traffic_images)}개의 파일 이름이 {output_txt_path}에 저장되었습니다.")
