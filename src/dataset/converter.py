import json
from pathlib import Path

from datasets import ClassLabel, Dataset, Features, Image, Sequence, Value
from tqdm import tqdm


def coco_to_parquet(images_dir: str, json_path: str, output_path: str):
    """
    Convert the ParasitoBank dataset from COCO format to Parquet format.

    Args:
        images_dir (str): Directory containing the image files.
        json_path (str): Path to the COCO JSON annotation file.
        output_path (str): Path where the Parquet file will be saved.
    """

    # Load JSON
    with open(json_path, "r") as f:
        data = json.load(f)

    images_json = data["images"]
    annotations_json = data["annotations"]
    label_names = [cat["name"] for cat in data["categories"]]

    # Parse Annotations
    annotationByImageId = {}
    for annotation in annotations_json:
        image_id = annotation["image_id"]
        annotationByImageId.setdefault(image_id, []).append({
            "label": annotation["category_id"] - 1,
            "bbox": [float(v) for v in annotation["bbox"]],
            "area": float(annotation["area"]),
        })

    records = []

    for img in tqdm(images_json, desc="Processing images"):
        image_id = img["id"]
        image_path = f"{images_dir}/{img['file_name']}"

        if not Path(image_path).exists():
            print(f"Warning: {image_path} not found. Skipping...")
            continue

        annotation = annotationByImageId.get(image_id, [])

        with open(image_path, "rb") as img_file:
            img_bytes = img_file.read()

        # Fix: dict of lists
        objects = {
            "label": [a["label"] for a in annotation],
            "bbox": [a["bbox"] for a in annotation],
            "area": [a["area"] for a in annotation],
        }

        records.append({
            "image": {"bytes": img_bytes, "path": img["file_name"]},
            "objects": objects,
        })

    # Feature Schema
    features = Features({
        "image": Image(),
        "objects": Sequence({
            "bbox": Sequence(Value("float32")),
            "label": ClassLabel(names=label_names),
            "area": Value("float32"),
        }),
    })

    ds = Dataset.from_list(records, features=features)

    print("Saving to Parquet...")
    ds.to_parquet(output_path)
    print("Saved to", output_path)
