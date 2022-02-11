
import matplotlib.pyplot as plt
import numpy as np

label_size=13
metric = 'Performance'

def PerformanceVariant():
    sname = ['MAP', 'MRR', 'NDCG']
    rein_search = [0.6, 0.7, 0.8]
    lambda_0 = [0.1, 0.2, 0.3]
    lambda_1 = [0.3, 0.4, 0.3]
    lambda_2 = [0.2, 0.4, 0.5]
    lambda_3 = [0.4, 0.3, 0.6]
    # blue1 = (209/255, 120/255, 25/255)
    # blue2 = (190/255, 120/255, 25/255)
    plt.figure(figsize=(18,4), dpi=80)
    # plt.figure(1)

    width = 0.15
    index = np.arange(len(sname))
    ax1 = plt.subplot(141)
    r1 = plt.bar(sname,rein_search,width,color='#999933',label='KRPS')
    r2 = plt.bar(index+width,lambda_0,width,color='#D17819',label='KRPS-'r'$\lambda_0$')
    r3 = plt.bar(index+width+width,lambda_1,width,color='#8DB9D3',label='KRPS-'r'$\lambda_1$')
    r4 = plt.bar(index+width+width+width,lambda_2,width,color='#94D119',label='KRPS-'r'$\lambda_2$')
    r5 = plt.bar(index+width+width+width+width,lambda_3,width,color='#AA92C4',label='KRPS-'r'$\lambda_3$')
    #显示图像
    plt.legend()
    plt.xlabel('(a) Electronics', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.0, 1.0, 0.2))
    # plt.legend(fontsize=10, loc='upper right', ncol=2)
    ax1.plot()
    # plt.plot()

    ax2 = plt.subplot(142)
    r1 = plt.bar(sname,rein_search,width,color='#999933',label='KRPS')
    r2 = plt.bar(index+width,lambda_0,width,color='#FF6600',label='KRPS-'r'$\lambda_0$')
    r3 = plt.bar(index+width+width,lambda_1,width,color='#3366CC',label='KRPS-'r'$\lambda_1$')
    r4 = plt.bar(index+width+width+width,lambda_2,width,color='#1A9900',label='KRPS-'r'$\lambda_2$')
    r5 = plt.bar(index+width+width+width+width,lambda_3,width,color='#8033CC',label='KRPS-'r'$\lambda_3$')
    #显示图像
    plt.legend()
    plt.xlabel('(b) Kindle Store', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.0, 1.0, 0.2))
    ax2.plot()

    ax3 = plt.subplot(143)
    r1 = plt.bar(sname,rein_search,width,color='#999933',label='KRPS')
    r2 = plt.bar(index+width,lambda_0,width,color='#FF6600',label='KRPS-'r'$\lambda_0$')
    r3 = plt.bar(index+width+width,lambda_1,width,color='#3366CC',label='KRPS-'r'$\lambda_1$')
    r4 = plt.bar(index+width+width+width,lambda_2,width,color='#1A9900',label='KRPS-'r'$\lambda_2$')
    r5 = plt.bar(index+width+width+width+width,lambda_3,width,color='#8033CC',label='KRPS-'r'$\lambda_3$')
    #显示图像
    plt.legend()
    plt.xlabel('(c) CDs & Vinyl', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.0, 1.0, 0.2))
    ax3.plot()

    ax4 = plt.subplot(144)
    r1 = plt.bar(sname,rein_search,width,color='#999933',label='KRPS')
    r2 = plt.bar(index+width,lambda_0,width,color='#FF6600',label='KRPS-'r'$\lambda_0$')
    r3 = plt.bar(index+width+width,lambda_1,width,color='#3366CC',label='KRPS-'r'$\lambda_1$')
    r4 = plt.bar(index+width+width+width,lambda_2,width,color='#1A9900',label='KRPS-'r'$\lambda_2$')
    r5 = plt.bar(index+width+width+width+width,lambda_3,width,color='#8033CC',label='KRPS-'r'$\lambda_3$')
    #显示图像
    plt.legend()
    plt.xlabel('(d) Cell Phones & Accessories', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.0, 1.0, 0.2))
    ax4.plot()
    plt.savefig('variant.jpg') 
    print('over')


###########performance changes with different lambda
def PerformanceDiffLambda():
    
    plt.figure(figsize=(24,4), dpi=80)
    # plt.figure(2)

    marker_edge_width = 0
    marker_size = 8 
    alpha = 0.9
    legend_order = [r'$\lambda_0$', r'$\lambda_1$', r'$\lambda_2$', r'$\lambda_3$']

    steps_data = [str(i) for i in range(10)]
    lambda_0 = [0.12, 0.24, 0.27, 0.34, 0.21, 0.18, 0.13, 0.10, 0.12, 0.10]
    lambda_1 = [0.02, 0.14, 0.17, 0.24, 0.11, 0.10, 0.08, 0.10, 0.12, 0.10]
    lambda_2 = [0.22, 0.26, 0.36, 0.42, 0.45, 0.40, 0.37, 0.35, 0.32, 0.29]
    lambda_3 = [0.08, 0.12, 0.14, 0.19, 0.22, 0.25, 0.23, 0.20, 0.17, 0.13]

    ax1 = plt.subplot(141)
    plt.plot(steps_data, lambda_0, linewidth=1, color='#999933', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_1, linewidth=1, color='#FF6600', linestyle='--', marker='o', label=legend_order[1], markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_2, linewidth=1, color='#333333', linestyle='--', marker='o', label=legend_order[2],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_3, linewidth=1, color='#3366CC', linestyle='--', marker='o', label=legend_order[3],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend()
    plt.xlabel('(a) Electronics', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.0, 0.5, 0.05))
    # plt.legend(fontsize=10, loc='upper right', ncol=2)
    ax1.plot()
    # plt.plot()

    ax2 = plt.subplot(142)
    plt.plot(steps_data, lambda_0, linewidth=1, color='#999933', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_1, linewidth=1, color='#FF6600', linestyle='--', marker='o', label=legend_order[1], markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_2, linewidth=1, color='#333333', linestyle='--', marker='o', label=legend_order[2],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_3, linewidth=1, color='#3366CC', linestyle='--', marker='o', label=legend_order[3],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend()
    plt.xlabel('(b) Kindle Store', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.0, 0.5, 0.05))
    ax2.plot()

    ax3 = plt.subplot(143)
    plt.plot(steps_data, lambda_0, linewidth=1, color='#999933', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_1, linewidth=1, color='#FF6600', linestyle='--', marker='o', label=legend_order[1], markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_2, linewidth=1, color='#333333', linestyle='--', marker='o', label=legend_order[2],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_3, linewidth=1, color='#3366CC', linestyle='--', marker='o', label=legend_order[3],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend()
    plt.xlabel('(c) CDs & Vinyl', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.0, 0.5, 0.05))
    ax3.plot()

    ax4 = plt.subplot(144)
    plt.plot(steps_data, lambda_0, linewidth=1, color='#999933', linestyle='--', marker='o', label=legend_order[0],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_1, linewidth=1, color='#FF6600', linestyle='--', marker='o', label=legend_order[1], markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_2, linewidth=1, color='#333333', linestyle='--', marker='o', label=legend_order[2],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    plt.plot(steps_data, lambda_3, linewidth=1, color='#3366CC', linestyle='--', marker='o', label=legend_order[3],markeredgecolor='black', markeredgewidth=marker_edge_width, markersize=marker_size, alpha=alpha)
    #显示图像
    plt.legend()
    plt.xlabel('(d) Cell Phones & Accessories', size=label_size)
    plt.ylabel(metric, size=label_size)
    plt.yticks(np.arange(0.0, 0.5, 0.052))
    ax4.plot()
    plt.savefig('variant1.jpg') 
    print('over')

if __name__ == "__main__":
    # PerformanceVariant()
    PerformanceDiffLambda()