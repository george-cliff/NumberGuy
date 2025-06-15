# NumberGuy

NumberGuy is a python based nerual network project, where a user generates a CNN model, using the mnist dataset, and can then draw a digit in the gui on the screen and the numberguy will guess their number

This README and project is still a heavy work in progress, this is my first project that im uploading to github
the readme itself will be updated soon with info on requirements how to run etc

for now my readme will also contain my current project todo list:

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

- [x] **Add user feedback**

  - [x] Add “Yes” and “No” buttons for feedback.
  - [x] Log whether the prediction was correct.
  - [x] If "No", suggest the next highest prediction.

- [ ] **Improve GUI usability**

  - [x] Add visual indicator for confidence.
  - [x] added digit to popup
  - [x] organised cleanup fuction to clear canvas and temp files on submission
  - [ ]
  - [ ] loading bar when generating a model
    - [ ] Learn about Keras callbacks—create a simple callback with `on_epoch_end()` that signals when an epoch completes
    - [ ] Add a `ttk.Progressbar` to the popup in determinate mode with max=16
    - [ ] Set up safe communication from the background training thread to the main UI thread (via queue or popup.after())
    - [ ] Connect the callback to update the progress bar after each epoch
    - [ ] After training finishes, close the progress popup and show a completion message

---

## 📌 Next Tasks (After Current Stage)

- [ ] **Reorganize gui.py into a class-based design**

  - [ ] Make a new class called `NumberGuyApp` to keep all the GUI parts and data together
  - [ ] Move the code from current `setup()` function into the class, using the `__init__` method and another setup method
  - [ ] Change all global variables like `window`, `canvas`, and `default_font` to be part of the class as `self.window`, `self.canvas`, `self.default_font`
  - [ ] Change the separate functions like `draw`, `btn_clear`, and `btn_submit` so they belong to the class as methods
  - [ ] Update button commands and other calls to use the class methods with `self.method_name` instead of the old global functions
  - [ ] Change the `popup_guess` function to be a method inside the class, so it can use the class variables easily
  - [ ] After moving everything, test app to make sure buttons and other parts still work fine
  - [ ] Add docustrings inside class and methods to help understand what each part does

- [ ] **Handle local user data**

  - [ ] Save user drawings and feedback locally.
  - [ ] Organize saved data for future retraining.
  - [ ] Delete temporary files when no longer needed.

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
