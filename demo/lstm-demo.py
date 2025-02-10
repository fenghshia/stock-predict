# --*-- Coding : UTF-8     --*--
# @Project     : stock-predict
# @File        : lstm-demo.py
# @Time        : 2025/2/8 下午6:23
# @IDE         : PyCharm
# @Description : Input Here
# --*-- Author : FengHShia --*--
import numpy as np
import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow.keras.layers import Dense, LSTM, Dropout, Input


tf.random.set_seed(7)
# 加载数据
x_train_data_set = np.load('./data-cache/x_train_data_set.npy')
x_test_data_set = np.load('./data-cache/x_test_data_set.npy')
y_train_data_set = np.load('./data-cache/y_train_data_set.npy')
y_test_data_set = np.load('./data-cache/y_test_data_set.npy')
# 创建模型
model = tf.keras.Sequential([
    Input(shape=(60, 1)),
    LSTM(units=80, activation='tanh', return_sequences=True),
    Dropout(rate=0.2),
    LSTM(units=100, activation='tanh', return_sequences=False),
    Dropout(rate=0.2),
    Dense(units=1)
], name="LSTM-Stock")
optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
model.compile(loss='mse', optimizer=optimizer)
# 输出模型规模
print(model.summary())
# 训练模型
history = model.fit(x_train_data_set, y_train_data_set, batch_size=64, epochs=20, validation_data=(x_test_data_set, y_test_data_set), validation_freq=1)
loss = history.history['loss']
acc = history.history['val_loss']
print(history.history.keys())

plt.plot(loss, label='Training loss')
plt.plot(acc, label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.savefig('lstm-loss.png')
