import os, sys
import tensorflow as tf
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# 1 显示所有信息
# 2 仅显示Warning & Error
# 3 仅显示Error
path = sys.argv[1]# 图片路径为第2个参数（test.py后第一个）
data = tf.gfile.FastGFile(path, 'rb').read()
# Loads label file, strips off carriage return
label = [line.rstrip() for line in tf.gfile.GFile("retrained_labels.txt")]
# Unpersists graph from file
with tf.gfile.FastGFile("retrained_graph.pb", 'rb') as f:
    graph_def = tf.GraphDef()
    graph_def.ParseFromString(f.read())
    tf.import_graph_def(graph_def, name='')
with tf.Session() as sess:
    # 将图片作为输入，输入到Graph中，并获得第一个Prediction
    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': data})
    # 按照置信度排序并输出
    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    for node_id in top_k:
        human_string = label[node_id]
        score = predictions[0][node_id]
        print('%s : %.5f' % (human_string, score))
