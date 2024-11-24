import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO



if __name__ == '__main__':
    model = YOLO('/root/autodl-tmp/runs/train/exp/weights/best.pt')
    model.val(data='/root/ultralytics_main/ultralytics-main/dataset/data.yaml',
              split='test',
              imgsz=640,
              batch=32,
              # iou=0.7,
              # rect=False,
              # save_json=True, # if you need to cal coco metrice
              project='/root/ultralytics_main/ultralytics-main/runs/test',
              name='exp',
              )