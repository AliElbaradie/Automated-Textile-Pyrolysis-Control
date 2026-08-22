# Automated Control of Textile Pyrolysis Experiments Using Machine Vision

**Bachelor Thesis**  
**University of Duisburg-Essen**  
**Completed: July 2024**

---

## Overview

This repository contains my bachelor's thesis on the development of an automated control system for textile pyrolysis experiments using **machine vision** and **digital PID control**.

The project combines **image acquisition, image processing, control engineering, LabVIEW and experimental hardware** to automatically regulate the movement of a textile sample during pyrolysis based on real-time camera measurements.

The project was conducted as part of a university research project investigating more environmentally friendly and health-conscious flame retardants for textiles.

The developed system uses an industrial camera to observe the pyrolysis process. The acquired images are processed in **LabVIEW** to extract process-relevant image features, which are then used as feedback variables for a closed-loop PID controller. The controller adjusts the speed of a stepper motor that controls the movement of the textile.

Two different image-based control strategies were investigated:

- **Burn mark width**
- **Mean pixel intensity**

The experimental evaluation showed that **mean pixel intensity provided better control performance** than burn mark width under the investigated conditions.

---

## Objectives

- Develop an automated closed-loop control system
- Implement a digital PID controller in LabVIEW
- Acquire and process camera images in real time
- Extract process-relevant variables from image data
- Automatically control textile movement using a stepper motor
- Investigate different image-based control variables
- Evaluate controller performance through experimental data analysis
- Experimentally validate the developed control strategy

---

## Technologies

### Programming & Software

- LabVIEW
- Python
- NumPy
- Matplotlib

### Control Engineering

- Digital PID Control
- Closed-loop Control
- PID Autotuning
- Feedback Control
- Self-optimizing Control

### Computer Vision & Image Processing

- Real-time Image Acquisition
- Image Preprocessing
- Grayscale Conversion
- Color Channel Extraction
- Blue Channel Analysis
- Region of Interest (ROI) / Image Section Analysis
- Spatial Averaging
- Pixel Intensity Analysis
- 1D Intensity Profile Extraction
- Savitzky–Golay Filtering
- Central-Difference Derivative
- Feature/Edge Localization using Signal Extrema
- Pixel-to-Physical-Unit Calibration
- Image-based Process Variable Extraction

### Hardware

- IDS Industrial Camera
- Stepper Motor with Integrated Controller
- Magnetic Absolute Encoder
- Custom-built Test Bench
- Tube Furnace
- Controlled Illumination

---

## Experimental Setup

The experimental setup consists of an **industrial camera, stepper motor, custom-built test bench, tube furnace, controlled illumination and a LabVIEW-based control system**.

The camera acts as the measurement device and continuously observes the textile during pyrolysis. The stepper motor acts as the actuator and controls the movement of the textile.

The computer running LabVIEW serves as the interface between the camera and motor and performs the image processing and closed-loop control.

The experimental camera featured a color sensor with a resolution of **1920 × 1200 pixels** and was connected to the computer via USB 3.0. The motor was operated through a USB interface and featured an integrated magnetic absolute encoder.

The figures below show the **actual laboratory setup** used during the experiments together with a **schematic overview** of the experimental system.

### Laboratory Setup

<p align="center">
<img src="images/experimental_setup_lab.jpg" width="70%">
</p>

### Experimental System Overview

<p align="center">
<img src="images/experimental_setup.png" width="80%">
</p>

---

## Control System

The experimental system is implemented as a **closed-loop feedback control system**.

The camera measures the current state of the pyrolysis process. LabVIEW processes the acquired image and determines the selected process variable. This value is compared with the desired setpoint, and the PID controller calculates the required motor speed.

The motor then moves the textile accordingly, changing the position of the pyrolysis zone and therefore influencing the measured process variable.

```text
                  Setpoint
                     │
                     ▼
              ┌─────────────┐
              │  Comparison │
              └──────┬──────┘
                     │ Error
                     ▼
              ┌─────────────┐
              │ LabVIEW PID │
              │  Controller │
              └──────┬──────┘
                     │ Motor Speed
                     ▼
              ┌─────────────┐
              │ Stepper     │
              │ Motor       │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │   Textile   │
              │  Pyrolysis  │
              └──────┬──────┘
                     │
                     ▼
              ┌─────────────┐
              │ Industrial  │
              │   Camera    │
              └──────┬──────┘
                     │ Image Data
                     ▼
              ┌─────────────┐
              │    Image    │
              │  Processing │
              └──────┬──────┘
                     │
                     └────────── Feedback
```

The motor speed is the manipulated variable, while the camera-derived process variable is fed back to the controller.

---

## Computer Vision & Image Processing

The machine-vision system was developed to extract measurable process information from the visual appearance of the pyrolyzing textile.

Two different image-processing approaches were investigated.

---

### 1. Burn Mark Width Detection

For burn mark width control, the acquired color image is first converted to **grayscale**.

This reduces the three color channels to a single intensity representation and allows the burn mark to be analyzed as a one-dimensional intensity profile.

A horizontal image section is extracted from the relevant area of the textile. The pixel intensities are then **arithmetically averaged along the vertical direction**, resulting in a one-dimensional intensity profile along the X-axis.

The burn mark appears as a region of reduced intensity compared with the surrounding unburned textile.

```text
Camera Image
     │
     ▼
Grayscale Conversion
     │
     ▼
Image Section / ROI
     │
     ▼
Vertical Spatial Averaging
     │
     ▼
1D Pixel-Intensity Profile
     │
     ▼
Savitzky–Golay Filtering
     │
     ▼
Central-Difference Derivative
     │
     ▼
Detection of Characteristic Extrema
     │
     ▼
Distance Between Detected Points
     │
     ▼
Burn Mark Width
```

### Signal Smoothing

The extracted intensity profile contains measurement noise, which becomes particularly problematic when calculating its derivative.

A **Savitzky–Golay filter** is therefore applied to smooth the signal while preserving important signal characteristics.

In the implemented analysis, a first-degree polynomial was used for local fitting. The filter reduces noise while maintaining the shape of the underlying intensity profile.

### Derivative-Based Edge Localization

After smoothing, the intensity profile is differentiated using the **central-difference method**.

The characteristic points corresponding to the burn mark boundaries appear as extrema in the derivative signal.

The distance between the detected extrema is used as the current **burn mark width**.

### Pixel-to-Physical Calibration

The detected burn mark width is initially obtained in pixels.

A calibration measurement was performed to determine the relationship between image pixels and physical distance.

The experimental calibration resulted in approximately:

```text
140 pixels ≈ 1 cm
14 pixels  ≈ 1 mm
```

This allows the detected burn mark width to be converted from pixels into physical units such as millimeters.

---

### 2. Mean Pixel Intensity

The second control strategy uses the **mean pixel intensity of an image region** as the process variable.

Before pyrolysis, the textile is relatively bright and therefore produces high pixel-intensity values. As pyrolysis progresses, a darker burn mark develops and the measured intensity decreases.

The objective is therefore to maintain a predefined mean pixel intensity corresponding to the desired degree of pyrolysis.

The image-processing sequence is:

```text
Camera Image
     │
     ▼
Color Channel Selection
     │
     ▼
Blue Channel Extraction
     │
     ▼
Image Region / ROI
     │
     ▼
Mean Pixel Intensity
     │
     ▼
PID Controller
```

### Blue Channel Selection

The camera provides three color channels.

The **blue channel** was selected for the control algorithm because it showed a stronger and faster intensity response to the formation of the burn mark than the other color channels.

The intensity decay of the different color channels was experimentally investigated. The blue channel showed the strongest sensitivity to the development of the burn mark and was therefore selected as the measurement basis for this control strategy.

### Spatial Averaging

After extracting the selected image region, the pixel intensities within the region are averaged.

This produces a single scalar process variable representing the current mean image intensity.

The calculated value is then passed to the PID controller.

---

## PID Autotuning

The LabVIEW **PID Autotuning VI** was used to determine suitable PID controller parameters for the experimental process.

The implemented controller uses a **self-optimizing PID approach**.

The tuning procedure starts with an initial set of controller parameters. The process is then excited and its dynamic response is observed. Based on the measured response, the autotuning routine adjusts the controller parameters to improve the control performance.

According to the experimental methodology, the initial controller parameters were determined iteratively and subsequently adapted by the LabVIEW self-tuning routine with the objective of minimizing the **mean control error over time**.

The user can also specify preferences regarding the desired controller response, such as the desired speed of response.

The PID controller parameters include:

- Proportional gain (**Kc**)
- Integral time (**Ti**)
- Derivative time (**Td**)

The autotuning interface also provides parameters for configuring the tuning procedure, including:

- Controller type
- Relay cycles
- Relay amplitude
- Control specification
- Process-variable noise level

### PID Autotuning Interface

<p align="center">
<img src="images/pid_block.png" width="80%">
</p>

> *LabVIEW PID Autotuning VI used to determine and optimize the controller parameters based on the measured process response.*

---

## LabVIEW Implementation

The complete control system was implemented in **LabVIEW**.

The application integrates camera acquisition, image processing, process-variable extraction, PID control, motor communication and user interaction.

The implemented software is responsible for:

- Camera image acquisition
- Real-time image visualization
- Image-region / ROI processing
- Grayscale conversion
- Color-channel extraction
- Pixel-intensity analysis
- Spatial averaging
- Signal smoothing
- Derivative calculation
- Burn mark width calculation
- Pixel-to-physical-unit conversion
- PID controller execution
- PID parameter configuration
- PID autotuning
- Motor speed control
- Motor communication and status monitoring
- Measurement and image storage
- Real-time process visualization
- Manual and automatic control operation

---

## LabVIEW Control Block Diagram

The following image shows a section of the complete LabVIEW block diagram responsible for the **actual closed-loop control operation**.

The shown section integrates image-processing results, process-variable calculation, PID control, speed calculation and motor-control logic.

<p align="center">
<img src="images/regelung_block_diagram.png" width="90%">
</p>

> *Section of the LabVIEW block diagram implementing the closed-loop control logic.*

---

## LabVIEW Front Panel

The LabVIEW front panel serves as the **user interface for operating and monitoring the experimental control system**.

It provides a centralized interface for configuring the controller, operating the motor and observing the camera-based measurement and image-processing results.

The interface provides:

- Live camera image display
- Processed Region of Interest (ROI) display
- Motor start/stop control
- Motor reset and quick-stop functions
- Motor direction control
- Motor speed configuration
- Motor speed monitoring
- Motor communication and error status
- Setpoint configuration
- PID parameter configuration
- PID autotuning control
- Closed-loop control activation
- Camera exposure-time configuration
- Image acquisition and storage
- Pixel-intensity visualization
- Derivative-signal visualization
- Image-processing parameter configuration
- Measurement and process monitoring

<p align="center">
<img src="images/regelung_front_panel.png" width="90%">
</p>

---

## Results

The developed control system successfully automated the textile pyrolysis experiment.

Two different process variables were investigated:

1. Burn mark width
2. Mean pixel intensity

For burn mark width control, experiments were conducted at different setpoints and temperatures, including **400 °C and 500 °C**.

For pixel-intensity control, different target intensities were investigated at different experimental temperatures.

The experimental evaluation demonstrated that the **mean pixel intensity approach provided better control performance** than the burn mark width approach under the investigated conditions.

The image-based control approach enabled the visual state of the pyrolysis process to be converted into a measurable process variable and used directly within a feedback control loop.

Experimental data were analyzed and visualized using **Python**, with:

- **NumPy** for numerical data processing
- **Matplotlib** for data visualization

The analyses were used to:

- Evaluate controller performance
- Compare different control variables
- Analyze steady-state behavior
- Evaluate control accuracy
- Compare stable and unstable controller behavior
- Assess the dynamic response of the control system

<p align="center">
<img src="images/results.png" width="90%">
</p>

> **Note**
>
> The figure illustrates controller behavior obtained from experimental measurements.

---

## Demonstration

A video demonstration of the complete experimental system is currently **not available**.

The project was conducted as a university laboratory research project, and the experimental equipment used during the experiments — including the industrial camera, stepper motor, test bench and associated laboratory hardware — is no longer available for recording a new demonstration.

The repository therefore focuses on the **LabVIEW implementation, computer-vision algorithms, control architecture, experimental setup, analysis results and project documentation**.

---

## Key Computer Vision Concepts

The project demonstrates practical application of classical image-processing techniques for closed-loop process control:

| Concept | Application in the Project |
|---|---|
| Image Acquisition | Real-time acquisition of textile pyrolysis images |
| Grayscale Conversion | Reduction of color image to a single intensity profile |
| Color Channel Extraction | Selection of the blue channel for intensity-based control |
| ROI / Image Section | Restriction of image analysis to the relevant textile region |
| Spatial Averaging | Reduction of image data to representative intensity values |
| 1D Intensity Profile | Analysis of intensity along the X-axis |
| Signal Smoothing | Noise reduction using a Savitzky–Golay filter |
| Numerical Differentiation | Central-difference derivative of the intensity profile |
| Feature Localization | Identification of burn mark boundaries from derivative extrema |
| Pixel Calibration | Conversion from pixel distance to physical dimensions |
| Mean Pixel Intensity | Extraction of a scalar process variable for feedback control |
| Experimental Signal Analysis | Evaluation of image-derived signals under different temperatures |

---

## Repository Structure

```text
Automated-Textile-Pyrolysis-Control/
│
├── README.md
│
├── LabVIEW/
│   └── Textile_Pyrolysis_Control.vi
│
├── images/
│   ├── experimental_setup_lab.jpg
│   ├── experimental_setup.png
│   ├── control_system.png
│   ├── image_processing.png
│   ├── pid_block.png
│   ├── regelung_block_diagram.png
│   ├── regelung_front_panel.png
│   └── results.png
│
└── docs/
    ├── bachelor_thesis.pdf
    ├── bachelor_thesis_Presentation.pdf
    └── bachelor_thesis_Presentation.pptx
```

> **Note:** The exact structure of the LabVIEW project files may depend on the LabVIEW project configuration and the files included in the repository.

---

## Documentation

The complete project documentation is available in the **docs** folder.

- 📄 [Bachelor Thesis (PDF)](docs/bachelor_thesis.pdf)
- 📄 [Final Presentation (PDF)](docs/bachelor_thesis_Presentation.pdf)
- 📊 [Presentation (PowerPoint)](docs/bachelor_thesis_Presentation.pptx)

---

## Project Status

**Completed – July 2024**

The experimental development and validation were completed as part of the bachelor's thesis.

The repository is maintained as a documentation and portfolio project containing the developed LabVIEW software, image-processing approach, control architecture, experimental results and thesis documentation.

---

## Author

**Ali Elbaradie**

Bachelor Thesis  
B.Sc. Mechanical Engineering  
University of Duisburg-Essen  

**Completed: July 2024**
