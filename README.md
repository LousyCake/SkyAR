# SkyAR GUI: Real-time Video Sky Replacement

SkyAR GUI is a user-friendly graphical interface for SkyAR, a vision-based method for real-time video sky replacement and harmonization. This repository provides an intuitive platform for users to leverage SkyAR's capabilities without the need for extensive coding knowledge.

![SkyAR GUI Demo](demo.png)

## Table of Contents
- [About SkyAR GUI](#about-skyar-gui)
- [How Does It Work?](#how-does-it-work)
- [System Requirements](#system-requirements)
- [How to Use It](#how-to-use-it)
- [Screenshots](#screenshots)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## About SkyAR GUI

SkyAR GUI is a graphical interface designed to simplify the process of utilizing the SkyAR method for video sky replacement. It provides an intuitive platform for users to replace sky backgrounds in videos with ease, without requiring extensive technical expertise.

## How Does It Work?

SkyAR GUI utilizes computer vision techniques to automatically generate realistic and dramatic sky backgrounds in videos. The process involves the following steps:

1. **Sky Matting:** Identifying and isolating the sky region in each frame of the video.
2. **Motion Estimation:** Estimating the motion dynamics in the video to ensure smooth blending of the replacement sky.
3. **Image Blending:** Seamlessly blending the replacement sky into the video frames, considering lighting and motion dynamics.

## System Requirements

SkyAR GUI has the following system requirements:

- **Operating System:** Windows, macOS, Linux
- **Python:** Version 3.6 or higher
- **Dependencies:**
  - `opencv-python`: OpenCV library for image and video processing.
  - `numpy`: Library for numerical computations.
  - `tkinter`: GUI toolkit for Python.
  - `Pillow`: Python Imaging Library (PIL) fork for image processing.
  - `matplotlib`: Library for plotting and visualization.

Please note that video processing tasks may require significant computational resources, including CPU and GPU capabilities, depending on the size and complexity of the input video.

## How to Use It

To use SkyAR GUI:

1. Clone this repository to your local machine.
2. Install the necessary dependencies using `pip install opencv-python numpy tkinter Pillow matplotlib`.
3. Navigate to the `SkyAR_GUI-main` directory.
4. Run `main.py` to launch the GUI.
5. Load your video file and select the desired sky replacement options.
6. Click "Apply" to generate the modified video with the new sky background.

## Screenshots

![SkyAR GUI Screenshot](gui_screenshot.png)

## Contributing

Contributions to SkyAR GUI are welcome! If you encounter any bugs, have feature requests, or want to contribute enhancements, feel free to submit pull requests.

## License

This project is licensed under the **MIT** License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

We thank the authors of the SkyAR method for their groundbreaking work.
