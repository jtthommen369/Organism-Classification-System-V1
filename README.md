# Organism Classification System V1

## Overview

The **Organism Classification System V1** is a rule-based Python program that classifies observable objects into **Animals, Plants, or Inanimate objects** based on a few simple traits. The system evaluates features such as movement, heat, color, size, angularity, and shape to determine the most likely category.  

This project demonstrates **logical feature-based classification** and serves as an original, beginner-friendly AI project.

---

## Features

- Rule-based classification system
- Input traits: movement, heat, color, size, angularity, shape
- Decision logic with a simple scoring system
- Handles cases where classification is uncertain
- Fully **explainable AI**: users can see exactly how traits influence the outcome

---

## How It Works

1. The user is prompted to enter observations for an object:
   - Movement (`yes`/`no`)  
   - Heat (`yes`/`no`)  
   - Color (`green`, `brown`, etc.)  
   - Size (`small`, `medium`, `large`)  
   - Angularity (`yes`/`no`)  
   - Shape (`spherical`, `flat`, `irregular`)

2. Each input is evaluated against simple rules and contributes to a score for:
   - Animal  
   - Plant  
   - Inanimate object

3. The category with the highest score is returned as the predicted classification.  

4. If there is a tie or unclear result, the program outputs **“Classification uncertain”**.

---

## Example Usage

```text
Movement detected? yes
Heat detected? yes
Color: brown
Size: medium
Angular? no
Shape: irregular

Likely Animal


Movement detected? no
Heat detected? no
Color: green
Size: medium
Angular? no
Shape: irregular

Likely Plant