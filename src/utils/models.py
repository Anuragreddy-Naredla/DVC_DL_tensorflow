import logging
import os
import tensorflow as tf


def get_VGG_16_model(input_shape, model_path):
    model = tf.keras.applications.vgg16.VGG16(input_shape=input_shape, weights="imagenet", include_top=False)
    model.save(model_path)
    logging.info(f"VGG16 base model saved at: {model_path}")
    return model

def prepare_model(model, CLASSES, freeze_all, freeze_till, learning_rate):
    if freeze_all:
        for layer in model.layers:
            layer.trainable = False
    elif (freeze_till is not None) and (freeze_till > 0):
        for layer in model.layers[:-freeze_till]:
            layer.trainable = False
    
    flatten_in = tf.keras.layers.Flatten()(model.output)
    prediction = tf.keras.layers.Dense(units = CLASSES, activation="softmax", )(flatten_in)

    full_model = tf.keras.models.Model(inputs = model.input, outputs = prediction)
    full_model.compile(optimizer = tf.keras.optimizers.SGD(learning_rate=learning_rate), loss = tf.keras.losses.CategoricalCrossentropy, 
    metrics=["accuracy"])
    logging.info("custom model is compiled and ready to be trained")

    return model