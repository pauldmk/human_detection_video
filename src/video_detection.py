from pathlib import Path

from imageai.Detection import VideoObjectDetection

from prepare_files import download_video, download_object_detection_models


def annotate_humans(
    input_file_path: Path,
    minimum_percentage_probability: int = 60,
    model_filename: str = "resnet50_coco_best_v2.1.0.h5",
):
    """
    Make use of imageai.Detection to annotate an input video with bounding boxes indicating the location of detected persons.
    Annotated video saved in /output folder.

    Args:
        input_file_path (Path): Path of input video to annotate
        minimum_percentage_probability (int, optional): Detection threshold probability (in %), model specific. Defaults to 60.
        model_filename (str, optional): Name of pretrained model stored in /data folder. Defaults to "resnet50_coco_best_v2.1.0.h5".
    """

    # indicate detection parameters in the output file name
    output_file_name = f"{input_file_path.stem}_{minimum_percentage_probability}%_{model_filename.split('.')[0]}"
    output_file_path = Path("output") / (output_file_name + ".avi")

    detector = VideoObjectDetection()
    detector.setModelTypeAsRetinaNet()  # change this method if using alternate models (e.g. YOLO)
    detector.setModelPath(Path("data") / model_filename)
    detector.loadModel()

    input_file_path = str(input_file_path.absolute())  # str required by imageai

    # perform detection on each frame of the video
    video_path = detector.detectObjectsFromVideo(
        input_file_path=str(input_file_path),
        custom_objects=detector.CustomObjects(
            person=True  # we're only interested in detecting humans
        ),
        output_file_path=str(Path("output") / output_file_name),
        frames_per_second=25,  # same fps as input video
        frame_detection_interval=1,
        log_progress=True,
        minimum_percentage_probability=minimum_percentage_probability,
    )


if __name__ == "__main__":
    # download models
    download_object_detection_models()

    # download video
    resolution = "1080p"
    filename = f"miss_dior_{resolution}.mp4"
    video_file_path = Path("data") / filename
    download_video(video_file_path, resolution=resolution)

    # annotate video
    annotate_humans(video_file_path, minimum_percentage_probability=60)
