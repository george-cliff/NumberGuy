from .mnist_loader import load_train_data, load_test_data, convert_img_data, convert_lab_data
import tensorflow as tf
import os
from .path import get_model_path, get_data_path
import datetime
from tensorflow.keras.models import load_model
import numpy as np


def prepare_data(data_path):
    #load and prepare training data
    train_img_data, train_lab_data = load_train_data(data_path)
    train_img_array = convert_img_data(train_img_data) / 255.0
    train_lab_array = convert_lab_data(train_lab_data)

    # Load and preapre test data
    test_img_data, test_lab_data = load_test_data(data_path)
    test_img_array = convert_img_data(test_img_data) / 255.0
    test_lab_array = convert_lab_data(test_lab_data)

    return train_img_array, train_lab_array, test_img_array, test_lab_array

def build_model():

    model = tf.keras.Sequential([
        tf.keras.layers.Input(shape=(28,28, 1)), # input shape: L, W, D

        tf.keras.layers.Conv2D(32, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Conv2D(64, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Conv2D(128, kernel_size=(3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D(pool_size=(2, 2)),

        tf.keras.layers.Flatten(),

        tf.keras.layers.Dense(256, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax")
    ])
    model.compile(optimizer="adam", loss="sparse_categorical_crossentropy", metrics=["accuracy"])
    return model

def test_model(model, test_img_array, test_lab_array):

    test_loss, test_accuracy = model.evaluate(test_img_array, test_lab_array)
    print(f"Test Accuracy: {test_accuracy}")
    print(f"Test Loss: {test_loss}")
    return test_loss, test_accuracy

def save_model_manual(model):
    while True:
        answer = input("Save model? [Y/n]: ").strip().lower()
        if answer == 'y' or answer == '':
            time = datetime.datetime.now()
            model_name = time.strftime("NumberGuy-Model-%Y%m%d-%H%M.h5")
            model_path = get_model_path()
            model_file=(os.path.join(model_path,model_name))
            model.save(model_file)
            print(f"Model saved successfully to {os.path.abspath(model_path)}")
            return model_file
        elif answer == 'n':
            print("Model not saved.")
            break
        else:
            print("Please type 'y' (yes), 'n' (no), or press Enter (yes).")

def save_model_auto(model):

    time = datetime.datetime.now()
    model_name = time.strftime("NumberGuy-Model-%Y%m%d-%H%M.h5")
    model_path = get_model_path()
    model_file=(os.path.join(model_path,model_name))
    model.save(model_file)
    return model_file

def generate():
    data_path = get_data_path()
    train_img_array, train_lab_array, test_img_array, test_lab_array = prepare_data(data_path)
    model = build_model()
    model.fit(train_img_array, train_lab_array, epochs=16)
    test_loss, test_accuracy = test_model(model, test_img_array, test_lab_array)
    model_file = save_model_auto(model)
    print("=====Model Training Completed===")
    print(f"Test Accuracy: {test_accuracy}")
    print(f"Test Loss: {test_loss}")
    return model_file


def predict_digit(img_array, model_files):
    model_path = get_model_path()
    model_files = sorted(
        [f for f in os.listdir(model_path) if f.endswith(".h5")])
    model_file = os.path.join(model_path, model_files[-1])
    model = load_model(model_file)
    prediction = model.predict(img_array)
    predicted_digit = np.argmax(prediction)
    digit = np.argmax(prediction)
    print(digit)
    return digit