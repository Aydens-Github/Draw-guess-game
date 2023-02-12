import paint
import numpy as np
import cv2
from pathlib import Path
from random import choice
import keras


draw_guess_game_path = fr'{Path(__file__).parents[0]}\draw_guess_game'
image_path = fr'{draw_guess_game_path}\dog.png'

label = 'dog'
# model = keras.models.load_model(fr'{draw_guess_game_path}\cifar10_trained_model')

# loading fashionmnist dataset
(train_images, train_labels), (extra_images, extra_labels) = keras.datasets..load_data()
train_images = np.concatenate((train_images, extra_images), axis=0)
train_labels = np.concatenate((train_labels, extra_labels), axis=0)

# Playing drawing game
image = paint.main(label)

# Making the images the correct format
image = cv2.resize(image, (32, 32), interpolation=cv2.INTER_LINEAR)
image = image.reshape(-1, 32, 32, 3)
image = image / 255 
train_images = train_images / 255

model = keras.models.Sequential([
    keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3), padding='same'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    keras.layers.MaxPooling2D((2, 2)),
    keras.layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    keras.layers.Flatten(),
    keras.layers.Dense(64, activation='softmax'),
    keras.layers.Dense(10),
])

model.compile(optimizer=keras.optimizers.Adam(),
            loss=keras.losses.SparseCategoricalCrossentropy(from_logits=True),
            metrics=['accuracy'])

reults = model.fit(train_images, train_labels, epochs=50)


# Testing the model
test_results = list(model.predict(image)[0])
guess_index = test_results.index(max(test_results))

if labels[guess_index] == label:
    print(f'\n\n The model guessed {labels[guess_index]}, the model was correct!')
else:
    print(f'\n\n The model guessed {labels[guess_index]}, the correct answer was {label}.')


# model.save(fr'{draw_guess_game_path}\cifar10_trained_model')
 