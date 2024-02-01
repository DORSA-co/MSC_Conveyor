import threading

import open3d as o3d
import numpy as np


class view3D:

    def __init__(self) -> None:
        pass


    def numpy2pcd(self,xyz:np.ndarray):
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(xyz)

        norm = np.zeros_like(xyz)
        norm[:,-1] = 1
        pcd.normals = o3d.utility.Vector3dVector( norm )
        return pcd
    
    def auto_bbox(self, pcd, bbox=None, border=10):
        if bbox is None:
            bbox = pcd.get_axis_aligned_bounding_box()
            bbox.min_bound = bbox.min_bound - border
            bbox.max_bound = bbox.max_bound + border 
        
        return bbox
    
    def pcd2mesh(self, pcd, alpha=0.5):
        mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(
        pcd, depth=7)
        mesh.compute_vertex_normals()
        mesh.paint_uniform_color(np.array([[0.5],[0.5],[0.5]]))
        return mesh

    def generate_bbox(self, x_range:tuple, y_range:tuple, z_range:tuple, border=10):
        bbox = o3d.geometry.AxisAlignedBoundingBox()
        bbox.min_bound = np.array([x_range[0] - border, y_range[0] - border, z_range[0] - border])
        bbox.max_bound = np.array([x_range[1] + border, y_range[1] + border, z_range[1] + border])
        return bbox
    
    def crop(self, mesh, bbox):
        return mesh.crop(bbox)
        
    
    def save_pcd(self, pcd, path):
        assert '.ply' in path
        o3d.io.write_point_cloud(path, pcd)


    def show_pointcloud(self, pcd):
        o3d.visualization.draw_geometries([pcd],
                                  zoom=0.3412,
                                  front=[0.4257, -0.2125, -0.8795],
                                  lookat=[2.6172, 2.0475, 1.532],
                                  up=[-0.0694, -0.9768, 0.2024],
                                  point_show_normal=False)

    def show_mesh(self, mesh):
        # o3d.visualization.draw_geometries([mesh],
        #                                   zoom=0.664,
        #                           front=[-0.4761, -0.4698, -0.7434],
        #                           lookat=[1.8900, 3.2596, 0.9284],
        #                           up=[0.2304, -0.8825, 0.4101],
        #                         mesh_show_back_face=True
        #                         )

        vis = o3d.visualization.Visualizer()
        vis.create_window()
        vis.add_geometry(mesh)
        vis.get_render_option().load_from_json("subPrograms/viewer/render_option.json")
            

        vis.run()

def depthImage2xyz(img:np.ndarray):
    xy = list(np.ndindex(img.shape[1], img.shape[0]))
    xy = np.array(xy)
    z = img[xy[:,1], xy[:,0]]
    z = np.expand_dims(z, axis=1)
    xyz = np.hstack((xy,z))
    return xyz


def randowm_down_sample(xyz, scale=0.5):
    count = xyz.shape[0]
    xyz = xyz[ np.random.randint(0, count, int(count*scale))]
    return xyz

def perfect_down_sample(xyz, scale=0.2):
    corect = xyz[ xyz[:,-1] == 0 ]
    defect = xyz[ xyz[:,-1] != 0 ]
    
    count = corect.shape[0]
    corect = corect[ np.random.randint(0, count, int(count*scale))]

    return np.vstack((corect, defect))


# def depthImage2xyz(img:np.ndarray):
#     xz = list(np.ndindex(img.shape[1], img.shape[0]))
#     xz = np.array(xz)
#     x = np.expand_dims(xz[:,0], axis=1)
#     z = np.expand_dims(xz[:,1], axis=1)
#     y = img[z[:,0], x[:,0]]
#     y = np.expand_dims(y, axis=1)
#     xyz = np.hstack((x,y,z))
#     return xyz

if __name__ == "__main__":
    print('start')
    #img = np.random.rand(640,1000)
    with open('../belt_images/depth/1.npy', 'rb') as f:
        img = np.load(f)
    import time

    t = time.time()
    # img = np.vstack((im/g,)*s8)
    h,w = img.shape
    xyz = depthImage2xyz(img)
    #xyz = randowm_down_sample(xyz,0.3)
    xyz = perfect_down_sample(xyz,0.1)

    

    v3 = view3D()
    pcd = v3.numpy2pcd(xyz)
    mesh = v3.pcd2mesh(pcd)
    bbox = v3.generate_bbox((0,w), (0,h), (-20,20), border=10)
    mesh = v3.crop(mesh, bbox)

    v3.show_mesh(mesh)
    #v3.show_pointcloud(pcd)

    # th = threading.Thread(target=v3.show_pointcloud, args=(pcd,))
    #th = threading.Thread(target=v3.show_mesh, args=(mesh,))
    #th.start()

    t = time.time()