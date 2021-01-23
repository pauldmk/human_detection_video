import os

from pytube import YouTube
import urllib


def download_video(
    video_file_path: str,
    url: str = "https://www.youtube.com/watch?v=h4s0llOpKrU",
    resolution: str = "720p",
):
    """
    Downloads video at specified Youtube url into into target_folder.

    :param video_file_path: path under which the video shall be downloaded
    :param url: Youtube url, defaults to "https://www.youtube.com/watch?v=h4s0llOpKrU"
    :param resolution: resolution of the video to download (must be available on Youtube), defaults to "720p"
    """
    video_url = url

    folder = os.path.dirname(video_file_path)
    _, filename = os.path.split(video_file_path)
    YouTube(video_url).streams.filter(res=resolution).first().download(
        folder, filename=filename.split(".")[0]
    )


def download_object_detection_models():
    """
    Downloads imageai-suitable pretrained object detection models into the /data folder.
    """

    # download backbone of RetinaNet model (ResNet50):
    urllib.request.urlretrieve(
        "https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5",
        os.path.join("data", "resnet50_coco_best_v2.1.0.h5"),
    )
    # # yolo didn't prove to give nearly as good results as RetinaNet:
    # urllib.request.urlretrieve(
    #     "https://github.com/OlafenwaMoses/ImageAI/releases/download/1.0/yolo.h5",
    #     os.path.join("data", "yolo.h5"),
    # )