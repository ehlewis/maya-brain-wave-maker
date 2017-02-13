# Maya Brainwave Creator (maya-brain-wave-maker)

## Creates a 3D object in Autodesk Maya from a CSV file

This script was initially created to take data from an Emotiv Insight EEG headset and transform it into a 3D model in Maya. 
However, past its intended use, it can be used to create a 3D object respresenting any CSV File in both an all channel polygon model on individual CV curve representation.
The curve functionality is still being tested, improved, and ironed out, so at the moment the only fully functioning representations are all channel polygon and single channel curve

## Usage

This is fairly self explanitory at the moment, however as it is inbetween versions the function calls are not great and some of the functions are not working correctly, but no major errors

### Setup

When run, the script will ask for the file path tot he CSV file and then how many channels (or columns) of data there are.
Next, in order for anything to work the CSV file must be linked and parsed by the intake function.
