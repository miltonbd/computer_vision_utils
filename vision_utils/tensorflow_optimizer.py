import tensorflow as tf

def get_optimizer(learning_rate):
    """Configures the optimizer used for training.

        Args:
            learning_rate: A scalar or `Tensor` learning rate.

        Returns:
            An instance of an optimizer.

        Raises:
            ValueError: if FLAGS.optimizer is not recognized.
        """

    optimizer = tf.train.MomentumOptimizer(
        learning_rate,
        momentum=0.9,
        name='Momentum')
    return optimizer