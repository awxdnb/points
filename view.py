import matplotlib.pyplot as plt
import numpy as np
import open3d as o3d
import torch

if __name__ == '__main__':
    # pts_o3d = o3d.io.read_point_cloud("C:/Users/82733/Desktop/CAD_0.ply", format="ply")
    pts_o3d = o3d.io.read_point_cloud("C:/Users/82733/Desktop/point/kitten.xyz", format="xyz")
    points = np.array(pts_o3d.points)
    normals = np.array(pts_o3d.normals)

    # sample_num = 2000
    # sample_idx = np.random.choice(points.shape[0], sample_num, replace=False)
    # points = points[sample_idx]

    plt.style.use('_mpl-gallery')

    xs = points[:, 0]
    ys = points[:, 1]
    zs = points[:, 2]
    # Plot
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    point_range = range(0, points.shape[0])
    ax.scatter(xs, zs, ys, c=zs,  marker="o")

    ax.axis('scaled')

    plt.show()
