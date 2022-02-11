
import matplotlib.pyplot as plt
import numpy as np

label_size=16
metric = 'Performance'

###########performance changes with different alpha
def PerformanceDiffLambda():
    
    plt.figure(figsize=(10,5), dpi=80)
    # plt.figure(2)

    marker_edge_width = 0
    marker_size = 8 
    alpha = 0.9
    # legend_order = [r'$\lambda_0$', r'$\lambda_1$', r'$\lambda_2$', r'$\lambda_3$']
    legend_order = ['NDCG@1', 'NDCG@3', 'Recall@3']

    # steps_data = [str(i) for i in range(11)]
    # steps_data = ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1']
    steps_data = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1]
    NDCG1 = [0.1900, 0.1923, 0.1936, 0.1930, 0.1928, 0.1889, 0.1867, 0.1823, 0.180, 0.1778, 0.1756]
    NDCG3 = [0.2834, 0.2993, 0.3101, 0.2995, 0.295, 0.2870, 0.2824, 0.2813, 0.2804, 0.2767, 0.2766]
    RECALL3 = [0.3912, 0.3962, 0.4007, 0.3957, 0.3933, 0.3917, 0.3900, 0.3867, 0.3854, 0.3767, 0.3700]


    ax1 = plt.subplot(121)
    plt.plot(steps_data, NDCG1, linewidth=1, color='#3910CE', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, NDCG3, linewidth=1, color='#FF6600', linestyle='--', marker='o', label=legend_order[1], markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, RECALL3, linewidth=1, color='#333333', linestyle='--', marker='o', label=legend_order[2],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)

    # plt.plot(steps_data, lambda_3, linewidth=1, color='#3366CC', linestyle='--', marker='o', label=legend_order[3],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend()
    plt.xlabel(r'(a) Movielens-1m on different $\alpha$', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0, 0.5, 0.05), fontsize=14)
    plt.xticks(fontsize=14)
    plt.legend(fontsize=12, loc='upper right', ncol=1)
    ax1.plot()
    # plt.plot()

    NDCG1 = [0.2791, 0.2813, 0.2902, 0.28670, 0.2856, 0.2789, 0.2734, 0.2700, 0.2685, 0.2654, 0.2612]
    NDCG3 = [0.4445, 0.4493, 0.4522, 0.4500, 0.4434, 0.4403, 0.4387, 0.4354, 0.4301, 0.4287, 0.4234]
    RECALL3 = [0.5580, 0.5695, 0.5721, 0.570, 0.5645, 0.5587, 0.5512, 0.5503, 0.5467, 0.5403, 0.5389]
    ax2 = plt.subplot(122)
    plt.plot(steps_data, NDCG1, linewidth=1, color='#3910CE', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, NDCG3, linewidth=1, color='#FF6600', linestyle='--', marker='o', label=legend_order[1], markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, RECALL3, linewidth=1, color='#333333', linestyle='--', marker='o', label=legend_order[2],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    # plt.plot(steps_data, lambda_3, linewidth=1, color='#3366CC', linestyle='--', marker='o', label=legend_order[3],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend(loc="upper right", fontsize=12)
    plt.xlabel(r'(b) Pinterest on different $\alpha$', size=label_size)
    # plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.25, 0.6, 0.05), fontsize=14)
    plt.xticks(fontsize=14)
    ax2.plot()

    plt.savefig('variant2.pdf') 
    print('over')


def PerformanceDiffLambdav2():
    
    plt.figure(figsize=(6,10), dpi=80)
    # plt.figure(2)

    marker_edge_width = 0
    marker_size = 8 
    alpha = 0.9
    legend_order = ['Movielens-1m', 'Pinterest']
    steps_data = ['0', '0.1', '0.2', '0.3', '0.4', '0.5', '0.6', '0.7', '0.8', '0.9', '1']

    MNDCG1 = [0.1900, 0.1923, 0.1936, 0.1930, 0.1928, 0.1913, 0.1900, 0.1897, 0.1890, 0.1870, 0.1856]
    MNDCG3 = [0.2834, 0.2993, 0.3101, 0.2995, 0.295, 0.2870, 0.2824, 0.2813, 0.2804, 0.2767, 0.2766]
    MRECALL3 = [0.3912, 0.3962, 0.4007, 0.3957, 0.3933, 0.3917, 0.3900, 0.3867, 0.3854, 0.3767, 0.3700]
    
    PNDCG1 = [0.2791, 0.2813, 0.2902, 0.28670, 0.2856, 0.2789, 0.2734, 0.2700, 0.2685, 0.2654, 0.2612]
    PNDCG3 = [0.4445, 0.4493, 0.4522, 0.4500, 0.4434, 0.4403, 0.4387, 0.4354, 0.4301, 0.4287, 0.4234]
    PRECALL3 = [0.5580, 0.5695, 0.5721, 0.570, 0.5645, 0.5587, 0.5512, 0.5503, 0.5467, 0.5403, 0.5389]

    ax1 = plt.subplot(311)
    plt.plot(steps_data, MNDCG1, linewidth=1.5, color='#3910CE', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)

    plt.plot(steps_data, PNDCG1, linewidth=1.5, color='#FF6600', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend()
    plt.xlabel(r'different $\alpha$', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.1, 0.3, 0.02))
    plt.legend(fontsize=10, loc='upper right', ncol=2)
    ax1.plot()

  
    ax2 = plt.subplot(312)
    plt.plot(steps_data, MNDCG3, linewidth=1.5, color='#3910CE', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, PNDCG3, linewidth=1.5, color='#FF6600', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend(loc="upper right")
    plt.xlabel(r'different $\alpha$', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.35, 0.60, 0.05))
    ax2.plot()

    ax3 = plt.subplot(313)
    plt.plot(steps_data, MRECALL3, linewidth=1.5, color='#3910CE', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, PRECALL3, linewidth=1.5, color='#FF6600', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend(loc="upper right")
    plt.xlabel(r'different $\alpha$', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.2, 0.5, 0.05))
    ax3.plot()

    plt.savefig('variant3.jpg') 
    print('over')

if __name__ == "__main__":
    PerformanceDiffLambda()
    # PerformanceDiffLambdav2()