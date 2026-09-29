import argparse
import cv2
from ultralytics import YOLO

def main(source=0, model_name="yolo11n.pt"):
    model = YOLO(model_name)
    cap = cv2.VideoCapture(source)

    if not cap.isOpened():
        raise RuntimeError("Could not open the video source.")

    while True:
        ok, frame = cap.read()
        if not ok:
            break

        results = model.track(
            frame,
            persist=True,
            conf=0.35,
            verbose=False
        )
        annotated = results[0].plot()

        cv2.putText(
            annotated,
            "YOLO Object Detection + Tracking | Press Q to quit",
            (15, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            (255, 255, 255),
            2
        )
        cv2.imshow("Object Detection and Tracking", annotated)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        default="0",
        help="0 for webcam, or path to a video file"
    )
    parser.add_argument(
        "--model",
        default="yolo11n.pt",
        help="Ultralytics pretrained YOLO model"
    )
    args = parser.parse_args()

    source = int(args.source) if args.source.isdigit() else args.source
    main(source, args.model)