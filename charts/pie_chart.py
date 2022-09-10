from matplotlib import pyplot as plt
from enterprises import enterprise_operation
import numpy as np


def select_all_enterprise():
    return enterprise_operation.list_all()

grupos = ['Produto A', 'Produto B', 'Produto C']
valores = [1, 10, 100]
plt.bar(grupos, valores)
plt.show()

print(select_all_enterprise())