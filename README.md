# Indian Sign Language Alphabet Recognizer

This project is a sign language alphabet recognizer using Python, openCV and tensorflow for training InceptionV3 model, a convolutional neural network model for classification.


## Requirements

This project uses python 3.6 and the PIP following packages:
* opencv
* tensorflow
* matplotlib
* numpy

See requirements.txt for required python packages

### Use virtualenv
```
virtualenv -p python3 virtual_env

source /virtual_env/bin/activate

pip install -r requirements.txt

```
### Running the code

To run the interface, use the following command:
```
python3 main.py

```
You will have options to train new signs, detect older signs
Your hand must be inside the rectangle. Keep position to write word, see demo for further information.
