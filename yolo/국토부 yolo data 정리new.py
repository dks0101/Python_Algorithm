import tkinter as tk
from PIL import Image, ImageTk
import os

class ImageLabeler:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Labeling Tool")

        # 이미지 파일 경로 직접 설정
        self.image_dir = "/home/user/다운로드/data_split_3"  # 이미지 디렉토리 경로 설정
        self.image_files = [f for f in os.listdir(self.image_dir) if f.endswith(('jpg', 'png', 'jpeg'))]
        self.current_image_idx = 0

        # Label to display the image
        self.image_label = tk.Label(root)
        self.image_label.pack()

        # Save image label with button 1
        self.button1 = tk.Button(root, text="good", command=lambda: self.save_label("good"))
        self.button1.pack(side="left")

        # Save image label with button 2
        self.button2 = tk.Button(root, text="bad", command=lambda: self.save_label("bad"))
        self.button2.pack(side="left")

        # 이미지 표시
        self.show_image()

    def show_image(self):
        if self.current_image_idx < len(self.image_files):
            image_path = os.path.join(self.image_dir, self.image_files[self.current_image_idx])
            image = Image.open(image_path)
            image = image.resize((600, 600))  # 이미지 크기 조정
            image_tk = ImageTk.PhotoImage(image)

            self.image_label.config(image=image_tk)
            self.image_label.image = image_tk  # Reference 유지
        else:
            self.image_label.config(text="No more images.")

    def next_image(self):
        self.current_image_idx += 1
        self.show_image()

    def save_label(self, label):
        if self.current_image_idx < len(self.image_files):
            image_name = self.image_files[self.current_image_idx]
            with open(f'{label}_labels.txt', 'a') as f:
                f.write(image_name + '\n')
            print(f"Saved {image_name} to {label}_labels.txt")
            self.next_image()  # 버튼 클릭 후 다음 이미지로 이동

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageLabeler(root)
    root.mainloop()
