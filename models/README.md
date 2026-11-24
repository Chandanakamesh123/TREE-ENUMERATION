
# AI Models - Tree Enumeration

## Primary Model
DeepForest

## Model Purpose
DeepForest is used to detect individual tree crowns
from aerial and drone imagery.

## Framework
- Python
- PyTorch
- DeepForest

## Model Input
- Drone images
- Satellite images
- Aerial forest images

## Model Output
- Tree bounding boxes
- Detection confidence scores
- Individual tree locations within the image

## Model Loading
The application initializes the DeepForest
pretrained model through its Python library.

## Model Weights
Pretrained model weights are managed by the
DeepForest library.

Custom-trained model weights can be stored
in this folder.

## Important
The model must be evaluated on the project's
actual forest imagery before reporting results.
