from pathlib import Path
import sys

# Get the absolute path of the current file
file_path = Path(__file__).resolve()

# Get the parent directory of the current file
root_path = file_path.parent

# Add the root path to the sys.path list if it is not already there
if root_path not in sys.path:
    sys.path.append(str(root_path))

# Get the relative path of the root directory with respect to the current working directory
ROOT = root_path.relative_to(Path.cwd())

# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'yolov8n.pt'
SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'
SEGMENTATION_CUSTOM_MODEL_N = MODEL_DIR / 'yolov8n-seg_cust.pt'
SEGMENTATION_CUSTOM_MODEL_M = MODEL_DIR / 'yolov8m-seg_cust.pt'

# Sources
IMAGE = 'Image'
VIDEO = 'Video'
WEBCAM = 'Webcam'
RTSP = 'RTSP'
# YOUTUBE = 'YouTube'

SOURCES_LIST = [IMAGE, VIDEO, WEBCAM]  # RTSP, YOUTUBE

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / 'metal402.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / 'metal402_pred.jpg'

# Videos config
VIDEO_DIR = ROOT / 'videos'
VIDEO_1_PATH = VIDEO_DIR / 'trash_1.mp4'
VIDEO_2_PATH = VIDEO_DIR / 'trash_2.mp4'

VIDEOS_DICT = {
                'video_1': VIDEO_1_PATH,
                'video_2': VIDEO_2_PATH,
            }
RTSP_STREAM_URL_DEF = "https://www.youtube.com/watch?v=KNJW1NynF6U"
# Webcam
WEBCAM_PATH = 0

