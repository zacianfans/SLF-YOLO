import warnings
warnings.filterwarnings('ignore')
from ultralytics import YOLO

if __name__ == '__main__':
    # model = YOLO("/root/ultralytics_main/ultralytics-main/new_cfg/yolov8s-CGLU-Star-C2f.yaml")
    model = YOLO("/root/ultralytics_main/ultralytics-main/new_cfg/yolov8s-SlimAsfNeck-CGLU.yaml")
    model.train(data='/root/ultralytics_main/ultralytics-main/dataset/data.yaml',
                cache=False,
                imgsz=640,
                epochs=300,
                batch=32,
                close_mosaic=10,
                workers=16,
                device='0',
                optimizer='SGD', # using SGD
                # resume=True, # last.pt path
                amp=False, # close amp
                # fraction=0.2,
                patience = 0,
                project='/root/autodl-tmp/runs/train',
                name='exp',
                )