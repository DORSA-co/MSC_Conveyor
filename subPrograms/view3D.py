import threading

import open3d as o3d
import numpy as np


class view3D:

    def __init__(self) -> None:
        pass


    def numpy2pcd(self,xyz:np.ndarray):
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(xyz)
        return pcd
    
    def save_pcd(self, pcd, path):
        assert '.ply' in path
        o3d.io.write_point_cloud(path, pcd)


    def show_pointcloud(self, pcd):
        o3d.visualization.draw_geometries([pcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024])


def depthImage2xyz(img:np.ndarray):
    xy = list(np.ndindex(img.shape[1], img.shape[0]))
    xy = np.array(xy)
    z = img[xy[:,1], xy[:,0]]
    z = np.expand_dims(z, axis=1)
    xyz = np.hstack((xy,z))
    return xyz


if __name__ == "__main__":

    img = np.random.rand(640,1000)
    xyz = depthImage2xyz(img)
    # x = np.linspace(-3, 3, 1000)
    # mesh_x, mesh_y = np.meshgrid(x, x)
    # z = np.sinc((np.power(mesh_x, 2) + np.power(mesh_y, 2)))
    # z_norm = (z - z.min()) / (z.max() - z.min())
    # xyz = np.zeros((np.size(mesh_x), 3))
    # xyz[:, 0] = np.reshape(mesh_x, -1)
    # xyz[:, 1] = np.reshape(mesh_y, -1)
    # xyz[:, 2] = np.reshape(z_norm, -1)


    v3 = view3D()
    pcd = v3.numpy2pcd(xyz)
    #v3.show_pointcloud(pcd)

    th = threading.Thread(target=v3.show_pointcloud, args=(pcd,))
    th.start()