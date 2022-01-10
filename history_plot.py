from matplotlib import pyplot as plt

def plot_loss(history):
    loss_train = history.history['loss']
    loss_val = history.history['val_loss']
    plt.plot(loss_train, 'r', label='Training loss')
    plt.plot(loss_val, 'b', label='validation loss')
    plt.title('Training and Validation loss')
    plt.xlabel('Epochs')
    plt.ylabel('Loss')
    plt.legend()
    plt.show()
    
def plot_accuracy(history):
    acc_train = history.history['accuracy']
    acc_val = history.history['val_accuracy']
    plt.plot(acc_train, 'r', label='Training Accuracy')
    plt.plot(acc_val, 'b', label='validation Accuracy')
    plt.title('Training and Validation Accuract')
    plt.xlabel('Epochs')
    plt.ylabel('Accuracy')
    plt.legend()
    plt.show()