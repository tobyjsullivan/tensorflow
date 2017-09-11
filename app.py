import tensorflow as tf

# Model parameters
W = tf.Variable([.3], dtype=tf.float32)
b = tf.Variable([-.3], dtype=tf.float32)
# Model input and output
x = tf.placeholder(tf.float32)
linear_model = W * x + b
y = tf.placeholder(tf.float32)

# loss
loss = tf.reduce_sum(tf.square(linear_model - y)) # sum of the squares
# optimizer
optimizer = tf.train.GradientDescentOptimizer(0.01)
train = optimizer.minimize(loss)

# training data
x_train = [1, 2, 3, 4]
y_train = [0, -1, -2, -3]
# training loop
init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init) # reset values to wrong

# Setup summary writer
tf.summary.scalar('loss function', loss)
merged = tf.summary.merge_all()
train_writer = tf.summary.FileWriter('/root/logs/train', sess.graph) 

for i in range(1000):
  summary, _ = sess.run([merged, train], {x: x_train, y: y_train})
  train_writer.add_summary(summary, i)

# evaluate training accuracy
summary, curr_W, curr_b, curr_loss = sess.run([merged, W, b, loss], {x: x_train, y: y_train})
test_writer = tf.summary.FileWriter('/root/logs/test', sess.graph)
test_writer.add_summary(summary, 0)
print("W: %s b: %s loss: %s"%(curr_W, curr_b, curr_loss))

