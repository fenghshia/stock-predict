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
from data_process import DataProcess


tf.random.set_seed(7)
# 加载数据
dp = DataProcess()
x_train_set, y_train_set = dp.train_data_random()
x_test_set, y_test_set = dp.test_data_orgnize()
# 创建模型
model = tf.keras.Sequential([
    Input(shape=(7, 1)),
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
history = model.fit(
    x_train_set, y_train_set, batch_size=64, epochs=50,
    validation_data=(x_test_set, y_test_set), validation_freq=1
)
loss = history.history['loss']
acc = history.history['val_loss']
print(history.history.keys())

plt.plot(loss, label='Training loss')
plt.plot(acc, label='Validation loss')
plt.title('Training and validation loss')
plt.legend()
plt.savefig('lstm-loss.png')
plt.close()

predict_price = model.predict(x_test_set)
# print(predict_price)
predict_price = dp.sc.inverse_transform(predict_price)
real_price = dp.sc.inverse_transform(dp.test_split[7:])
# print(real_price_shape)
# real_price = [i[0] for i in real_price_shape]
plt.plot(real_price, label='Real price', color='blue')
plt.plot(predict_price, label='Predicted price', color='red')
plt.legend()
plt.savefig('lstm-price.png')
