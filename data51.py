import fiftyone as fo 
import fiftyone.zoo as foz

source_dir = "/data/BDD100K/bdd100k"

dataset = foz.load_zoo_dataset(
    "bdd100k",
    split="validation",
    source_dir = source_dir,
)

session = fo.launch_app(dataset)

# Blocks execution until the App is closed
session.wait()
