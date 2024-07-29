Simple Image Encryption Using Python and tkinter
Objective:
Encrypt an image file by altering its data using a simple XOR operation with a user-provided numeric key.

Components:
User Interface (UI):

Built with tkinter.
Includes a button to select an image and an input field for the encryption key.
Process:

File Selection: User selects an image file via a file dialog.
Encryption:
The image data is read as a bytearray.
Each byte is XORed with the numeric key provided by the user.
Saving: The encrypted data overwrites the original image file.
Key Points:
Basic XOR Encryption: Uses a simple and reversible method to alter image data.
Input Handling: Ensures the key is numeric and handles file reading/writing.
Usage:
Run the script.
Select an image file and enter a numeric key.
The image is encrypted using the key.
This project provides a basic introduction to image data manipulation and GUI design in Python.
