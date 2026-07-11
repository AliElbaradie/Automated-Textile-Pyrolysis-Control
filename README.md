# Automated Control of Textile Pyrolysis Experiments Using Machine Vision

Bachelor Thesis  
University of Duisburg-Essen  
Completed: July 2024

---

# Overview

This repository contains my bachelor's thesis on the development of an automated closed-loop control system for textile pyrolysis experiments using machine vision and digital control engineering.

The objective of the project was to automate the movement of a textile sample during pyrolysis by processing real-time camera images and controlling a stepper motor with a digital PID controller implemented in LabVIEW.

The project combines image processing, automation, control engineering and experimental validation to improve the stability and accuracy of textile pyrolysis experiments.

---

# Objectives

- Develop an automated closed-loop control system for textile pyrolysis experiments
- Implement a digital PID controller in LabVIEW
- Acquire and process camera images in real time
- Evaluate different image-based control variables
- Validate the control system through experimental testing
- Compare controller performance under different operating conditions

---

# Key Features

- Automated textile movement control
- Digital PID controller
- Real-time image acquisition
- Machine vision-based feedback
- Image processing for process monitoring
- Industrial camera integration
- Stepper motor control
- Experimental validation and performance evaluation

---

# Technologies

## Programming & Software

- LabVIEW

## Control Engineering

- Digital PID Control
- Closed-loop Control
- Feedback Control
- Process Automation

## Image Processing

- Machine Vision
- Image Acquisition
- Pixel Intensity Analysis
- Burn Mark Detection
- Image Filtering

## Hardware

- IDS Industrial Camera
- Stepper Motor with Absolute Encoder
- Custom Test Bench
- Tube Furnace
- Lighting System

---

# Experimental Setup

The experimental setup consists of seven main components:

## Textile Sample

- Cotton textile mounted on a roll
- Material investigated during pyrolysis

## Stepper Motor

- Controls the movement of the textile
- USB communication with LabVIEW
- Integrated absolute encoder

## Industrial Camera

- IDS industrial color camera
- Resolution: 1920 × 1200 pixels
- Image acquisition up to 72 fps
- Real-time monitoring of the pyrolysis process

## Mechanical Test Bench

- Custom-built frame
- Guides the textile through the heating zone

## Tube Furnace

- Custom-built furnace
- Heating temperature up to 900 °C
- Pyrolysis under Argon or synthetic air

## Illumination System

- Constant lighting conditions
- Improved image quality and measurement accuracy

## Control Computer

- Executes the LabVIEW application
- Performs image processing
- Implements the PID controller
- Controls the stepper motor

---

# Control System

The closed-loop control system consists of:

- Sensor: Industrial Camera
- Controller: LabVIEW Digital PID Controller
- Actuator: Stepper Motor
- Plant: Textile Pyrolysis Process

The controller continuously processes camera images, calculates the current process value and automatically adjusts the motor speed to maintain the desired operating condition.

---

# Methodology

The developed software performs the following steps continuously:

1. Capture camera images
2. Process the acquired images
3. Extract image features
4. Calculate the process variable
5. Compare the measured value with the reference value
6. Calculate the PID controller output
7. Adjust the motor speed
8. Repeat the control cycle

Two different control variables were investigated:

- Burn mark width
- Average pixel intensity

The controller performance of both approaches was experimentally compared.

---

# Results

The developed system successfully automated the textile pyrolysis experiment.

The experimental evaluation showed that:

- The automated controller maintained stable process conditions.
- Real-time image processing enabled continuous process monitoring.
- Average pixel intensity achieved higher control accuracy than burn mark width.
- The developed control strategy improved the stability and dynamic response of the process.
- The project demonstrated the feasibility of image-based closed-loop control for textile pyrolysis experiments.

---

# Skills Demonstrated

- Control Engineering
- PID Controller Design
- LabVIEW Programming
- Machine Vision
- Image Processing
- Process Automation
- Experimental Design
- Data Analysis
- System Integration
- Technical Documentation
- Problem Solving

---

# Repository Structure

```
Automated-Textile-Pyrolysis-Control/
│
├── README.md
├── Bachelor_Thesis.pdf
├── images/
│   ├── experimental_setup.png
│   ├── control_system.png
│   ├── image_processing.png
│   ├── results.png
│   └── thesis_cover.png
└── LICENSE
```

---

# Figures

## Thesis Cover

*(Insert thesis cover image here.)*

---

## Experimental Setup

*(Insert experimental setup image here.)*

---

## Control System

*(Insert control loop diagram here.)*

---

## Image Processing

*(Insert image processing workflow here.)*

---

## Experimental Results

*(Insert graphs or comparison figures here.)*

---

# About Me

**Author:** Ali Elbaradie

Bachelor Thesis

B.Sc. Mechanical Engineering

University of Duisburg-Essen

Completed: July 2024

---

## Contact

- LinkedIn: https://linkedin.com/in/ali-elbaradie-3627b11b4
- GitHub: https://github.com/AliElbaradie
