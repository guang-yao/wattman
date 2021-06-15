import json
import cv2


class PicJoin:
    def __init__(self, json_file):
        with open(json_file, 'r')as f:
            json_dict = json.load(f)
        self.rec = {}
        for box in json_dict['boxes']:
            self.rec[box['name']] = box['rectangle']

    def print_boxb(self):
        print(self.rec['box_b'])

    def join_pic(self, pic1_path, pic2_path):
        pic1 = cv2.imread(pic1_path)
        pic2 = cv2.imread(pic2_path)

        left, top = self.rec['box_b']['left_top']
        right, bottom = self.rec['box_b']['right_bottom']
        pic1 = cv2.resize(pic1, (bottom - top, right - left))
        pic2[left:right, top:bottom] = pic1
        return pic2



if __name__ == '__main__':
    json_file = 'boxes.json'
    pj = PicJoin(json_file)
    pj.print_boxb()
    pic1 = pj.join_pic('cat.jpg', 'cat.jpg')
