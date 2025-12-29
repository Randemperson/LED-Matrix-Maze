# LED Matrix Maze – Custom PCB Project

![3D Render](renders/isometric_render.png)

- **Tools:** KiCad, Raspberry Pi, MAX7219, Thonny and VSCode IDE
- **Focus:** PCB Design, Embedded Systems, Interactive Hardware

## Overview
This project implements an interactive LED matrix maze system using a custom
PCB designed in KiCad. The board integrates an LED driver, microcontroller
interface, and user inputs, and is designed for in-house prototyping and
iteration.

## Prototyping
Before PCB fabrication, the circuit was validated using a breadboard prototype
to test LED matrix control, button inputs, and maze logic. This prototype was
used to verify functionality prior to committing to PCB fabrication.

![Breadboard Prototype](photos/breadboard_prototype.jpg)

## Fabrication Plan
The PCB is designed for rapid prototyping using professional PCB milling and
laser equipment available through the GT Hive makerspace. The design is prepared
for fabrication on an LPKF ProtoMat S103 and ProtoLaser U4 system, enabling fast
iteration and testing prior to final assembly.

## What I Did
- Designed schematics and PCB layout in KiCad
- Integrated MAX7219 LED driver
- Routed signals with attention to layout clarity and manufacturability
- Generated fabrication files and assembled the board
- Wrote firmware to control maze logic and LED output

## Repository Structure
- `/renders` – 3D PCB renders
- `/photos` – Assembled board photos
- `/schematic` – Schematics
- `/pcb` – PCB layout files
- `/code` – Firmware and control logic

## Status
Design complete and ready for fabrication in january spring semester starts.
