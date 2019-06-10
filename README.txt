环境： python 3.x


# 依赖
pip3 install tensorflow
pip3 install six
pip3 install bumpy
...


# 执行命令, 样例

python test.py flower_photos_test/test-00111.jpg


# 获得结果

WARNING:tensorflow:From test.py:8: FastGFile.__init__ (from tensorflow.python.platform.gfile) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.gfile.GFile.
roses : 0.99959
tulips : 0.00039
sunflowers : 0.00002
daisy : 0.00000
dandelion : 0.00000

# 根据输出的置信度排序，获得结果：roses