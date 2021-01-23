import os
from imageai.Detection import VideoObjectDetection
from prepare_files import download_video, download_object_detection_models


def annotate_humans(
    input_file_path: str,
    minimum_percentage_probability: int = 60,
    model_filename: str = "resnet50_coco_best_v2.1.0.h5",
):
    """
    Make use of imageai.Detection to annotate an input video with bounding boxes
    indicating the location of detected persons.
    Annotated video saved in /output folder.

    :param input_file_path: path of input video to annotate
    :param minimum_percentage_probability: detection threshold probability (in %), model specific, defaults to 50
    :param model_filename: name of pretrained model (backbone) stored in /data folder, defaults to "resnet50_coco_best_v2.1.0.h5"
    """

    # indicate detection parameters in the output file name
    output_file_name = f"annotated_video_{minimum_percentage_probability}_{model_filename.split('.')[0]}"
    output_file_path = os.path.join("output", output_file_name + ".avi")

    detector = VideoObjectDetection()
    detector.setModelTypeAsRetinaNet()  # change this method if using alternate models (e.g. YOLO)
    detector.setModelPath(os.path.join("data", model_filename))
    detector.loadModel()

    # perform detection on each frame of the video
    video_path = detector.detectObjectsFromVideo(
        input_file_path=input_file_path,
        custom_objects=detector.CustomObjects(
            person=True  # we're only interested in detecting humans
        ),
        output_file_path=os.path.join("output", output_file_name),
        frames_per_second=25,  # same fps as input video
        frame_detection_interval=1,
        log_progress=True,
        minimum_percentage_probability=minimum_percentage_probability,
    )


if __name__ == "__main__":
    # download models
    download_object_detection_models()

    # download video
    video_file_path = os.path.join("data", "miss_dior.mp4")
    download_video(video_file_path, resolution="1080p")

    # annotate video
    annotate_humans(video_file_path, minimum_percentage_probability=60)