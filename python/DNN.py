import tensorflow as tf
import numpy as np
from numpy import genfromtxt

input_c = 6
hidden_c = 500
output_c = 2

x_data = genfromtxt('./data/train_data.csv', delimiter=',')
#print(x_data)

y_data = genfromtxt('./data/train_result.csv', delimiter=',')
#print(y_data)

#########
# 신경망 모델 구성
######
X = tf.placeholder(tf.float32)
Y = tf.placeholder(tf.float32)

# 첫번째 가중치의 차원은 [특성, 히든 레이어의 뉴런갯수]
W1 = tf.Variable(tf.random_uniform([input_c, hidden_c], -1., 1.))
# 두번째 가중치의 차원을 [첫번째 히든 레이어의 뉴런 갯수, 분류 갯수
W2 = tf.Variable(tf.random_uniform([hidden_c, output_c], -1., 1.))

# 편향을 각각 각 레이어의 아웃풋 갯수로 설정합니다.
b1 = tf.Variable(tf.zeros([hidden_c]))
b2 = tf.Variable(tf.zeros([output_c]))

# 신경망의 히든 레이어에 가중치 W1과 편향 b1을 적용합니다
L1 = tf.add(tf.matmul(X, W1), b1)
L1 = tf.nn.relu(L1)

# 최종적인 아웃풋을 계산합니다.
# 히든레이어에 두번째 가중치 W2와 편향 b2를 적용하여 3개의 출력값을 만들어냅니다.
model = tf.add(tf.matmul(L1, W2), b2)

# 텐서플로우에서 기본적으로 제공되는 크로스 엔트로피 함수를 이용해
# 복잡한 수식을 사용하지 않고도 최적화를 위한 비용 함수를 다음처럼 간단하게 적용할 수 있습니다.
cost = tf.reduce_mean(
	tf.nn.softmax_cross_entropy_with_logits(labels=Y, logits=model))

optimizer = tf.train.AdamOptimizer(learning_rate=0.01)
train_op = optimizer.minimize(cost)


#########
# 신경망 모델 학습
######
saver = tf.train.Saver()
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

saver.restore(sess, './model/model')
for step in range(1000):
	sess.run(train_op, feed_dict={X: x_data, Y: y_data})

	if ((step + 1) % 100 == 0):
		print(step + 1, sess.run(cost, feed_dict={X: x_data, Y: y_data}))
		#saver.save(sess, './model/model')

print(sess.run(cost, feed_dict={X: x_data, Y: y_data}))
saver.save(sess, './model/model')

#########
# 결과 확인
######
x_data2 = genfromtxt('./data/train_data.csv', delimiter=',')
y_data2 = genfromtxt('./data/train_result.csv', delimiter=',')

prediction = tf.argmax(model, 1)
target = tf.argmax(Y, 1)
#print('예측값:', sess.run(prediction, feed_dict={X: x_data2}))
#print('실제값:', sess.run(target, feed_dict={Y: y_data2}))

is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data2, Y: y_data2}))
###
x_data2 = genfromtxt('./data/test_data.csv', delimiter=',')
y_data2 = genfromtxt('./data/test_result.csv', delimiter=',')

prediction = tf.argmax(model, 1)
target = tf.argmax(Y, 1)
#print('예측값:', sess.run(prediction, feed_dict={X: x_data2}))
#print('실제값:', sess.run(target, feed_dict={Y: y_data2}))

is_correct = tf.equal(prediction, target)
accuracy = tf.reduce_mean(tf.cast(is_correct, tf.float32))
print('정확도: %.2f' % sess.run(accuracy * 100, feed_dict={X: x_data2, Y: y_data2}))