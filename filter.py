import fiftyone as fo
import fiftyone.zoo as foz

source_dir = "/data/BDD100K/bdd100k"

dataset = foz.load_zoo_dataset(
    "bdd100k",
    split="validation",
    source_dir = source_dir,
)

view = dataset.match(F("timeofday").label == "night")

export_dir = "/data/BDD100K/bdd100k/night"

view.export(
    export_dir = export_dir,
    dataset_type=fo.types.ImageDirectory
)

print(f"Filtered images have been exported to {export_dir}")