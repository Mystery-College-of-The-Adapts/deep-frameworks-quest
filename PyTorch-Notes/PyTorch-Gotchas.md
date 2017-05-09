## Data

Generally, when we have to deal with image, text, audio or video data, we can use standard python packages that load data into ```NumPy array```. Then we can convert this array into ```torch.*Tensor```.

### Packages for images:
- [Pillow]()
- [OpenCV]()


### Packages for audio:
- [Scipy]()
- [Librosa]()


### Packages for text:
- [raw Python]()
- [NLTK]()
- [SpaCy]()



Specifically for vision, PyTorch has a package called torchvision, that has data loaders for common datasets such as **Imagenet, CIFAR10, MNIST**, etc. and **data transformers for images, viz., ```torchvision.datasets``` and ```torch.utils.data.DataLoader```**.