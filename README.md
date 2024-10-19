# speech-recognition

Here's a sample `README.md` for your GitHub project:

---

# Speech to Text Converter with GUI

This project is a simple **Speech to Text Converter** built using Python. It features a **Graphical User Interface (GUI)** built with `tkinter` that listens to your speech, converts it to text, and displays the formatted text in real-time.

## Features

- Real-time speech-to-text conversion using the Google Speech Recognition API.
- A simple GUI to display the recognized and formatted text.
- Filters out filler words like "um", "uh", and "like" to make the text more professional.
- Automatically capitalizes sentences and adds punctuation to the end.

## Technologies Used

- **Python**: The core language for the application.
- **SpeechRecognition**: For converting speech to text.
- **PyAudio**: For capturing audio from the microphone.
- **Pyttsx3**: For initializing the text-to-speech engine (though not actively used in this project).
- **Tkinter**: For creating the graphical user interface.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/speech-to-text-gui.git
   cd speech-to-text-gui
   ```

2. Install the required dependencies:
   ```bash
   pip install SpeechRecognition pyttsx3 pyaudio
   ```

   - If you face issues installing `pyaudio`, download the appropriate `.whl` file from [here](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) and install it:
     ```bash
     pip install <path_to_wheel_file>
     ```

3. (Optional) If `tkinter` is not already installed, you can install it (Linux only):
   ```bash
   sudo apt-get install python3-tk
   ```

## How to Use

1. Run the script:
   ```bash
   python project_with_ui.py
   ```

2. A window will appear with a button labeled **Start Listening**. Click the button to start the speech recognition process.

3. Speak into your microphone, and the recognized speech will be displayed in the text area in real-time.

4. The text is automatically formatted by capitalizing the first letter and adding punctuation at the end. Filler words like "um", "uh", and "like" are removed to make the text more professional.

## Example

- Before: "um I would like to uh discuss the project"
- After: "I would discuss the project."

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests! Any contributions are welcome to help improve this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

