# NumberGuy To-Do List

## ✅ Completed Tasks

### 🎯 Core Functionality

- [x] **Load and visualize MNIST dataset**

  - [x] Download MNIST dataset.
  - [x] Visualize sample digits using `matplotlib`.

- [x] **Build and train CNN model**

  - [x] Define CNN architecture.
  - [x] Compile the model with loss and optimizer.
  - [x] Train on MNIST training data.
  - [x] Evaluate on test data and measure accuracy.

- [x] **Create basic GUI with Tkinter**

  - [x] Implement a canvas for user to draw digits.
  - [x] Add buttons: "Submit", "Generate Model", and "Clear".

- [x] **Connect GUI with model**

  - [x] Capture user drawing as image.
  - [x] Preprocess image to match CNN input format.

- [x] **Display prediction**

  - [x] Show model's predicted digit in the GUI.

---

## 🔨 Current Tasks (In Progress / Next Steps)

- [ ] **Add user feedback**

  - [ ] Add “Yes” and “No” buttons for feedback.
  - [ ] Log whether the prediction was correct.
  - [ ] If "No", suggest the next highest prediction.

- [ ] **Handle local user data**
  - [ ] Save user drawings and feedback locally.
  - [ ] Organize saved data for future retraining.
  - [ ] Delete temporary files when no longer needed.

---

## 📌 Next Tasks (After Current Stage)

- [ ] **Improve GUI usability**

  - [ ] Add visual indicator for confidence.
  - [ ] loading bar when generating a model

- [ ] **documentation**

  - [ ] add docustrings to each of the fucntions
  - [ ] create a readme with step by step on how it works

---

## 🚀 Future Features (Planned for NumberGuy 2.0)

### 📁 Smarter Data Storage

- [ ] Use structured folders or a lightweight database to store user inputs.
- [ ] Add metadata (timestamp, feedback, etc.) to each saved entry.

### 🔁 Adaptive Model Training

- [ ] Add a "Retrain Model" button in the GUI.
- [ ] Allow retraining with collected user feedback.
- [ ] Visualize training progress and display new accuracy.
- [ ] Let users select between different trained models.

### 🧽 GUI Enhancements

- [ ] Improve drawing canvas to better mimic MNIST data.
  - [ ] Adjustable brush size.
  - [ ] Optional eraser tool.
- [ ] Add animations or friendly messages for user actions.

### 🔢 Advanced Capabilities

- [ ] Recognize multiple digits (e.g. "45").
- [ ] Display confidence scores or probabilities for predictions.

---
