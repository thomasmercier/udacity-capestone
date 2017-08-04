import tensorflow as tf

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def fully_connected(in_layer, layer_size, activation):
    '''
    create a stack of fully connected flat layers
    in_layer is a 2D tensor
    layer_size is a list of the different layer sizes
    '''

    in_shape = in_layer.shape.as_list()
    N = len(layer_size)

    W = [None]*N
    b = [None]*N
    h = [None]*N

    W[0] = weight_variable([in_shape[1], layer_size[0]])
    b[0] = bias_variable([layer_size[0]])
    h[0] = activation(tf.matmul(enc_h_flat, enc_W_fcN[0]) + enc_b_fcN[0] )

    for i in range(1, N):
        W[i] = weight_variable([layer_size[i-1], layer_size[i]])
        b[i] = bias_variable(layer_size[i])
        h[i] = activation(tf.matmul(h[i-1], W[i]) + b[i] )

    return h[N-1]
