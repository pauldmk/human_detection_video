import os
from pathlib import Path

from pytube import YouTube
import urllib


def download_object_detection_models(
    url: str = "https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5",
):
    """
    Downloads imageai-suitable pretrained object detection models into the /data folder.

    Args:
        url (str, optional): url of file to download.
        Defaults to "https://github.com/OlafenwaMoses/ImageAI/releases/download/essentials-v5/resnet50_coco_best_v2.1.0.h5".
    """

    # download backbone of RetinaNet model (ResNet50):
    target_path = Path("data") / url.split("/")[-1]
    if not target_path.exists():
        print("Downloading pretrained model backbone...")
        urllib.request.urlretrieve(
            url,
            target_path,
        )


def download_video(
    video_file_path: Path,
    video_url: str = "https://www.youtube.com/watch?v=h4s0llOpKrU",
    resolution: str = "720p",
):
    """
    Downloads video at specified Youtube url into into target_folder.

    Args:
        video_file_path (Path): Path under which the video shall be downloaded.
        video_url (str, optional): Youtube url. Defaults to "https://www.youtube.com/watch?v=h4s0llOpKrU".
        resolution (str, optional): Resolution of the video to download (must be available on Youtube). Defaults to "720p".
    """

    if not video_file_path.exists():
        print("Downloading video...")
        folder = video_file_path.parents[0]
        YouTube(video_url).streams.filter(res=resolution).first().download(
            folder, filename=video_file_path.stem
        )
