import numpy as np
import open3d as o3d
import octree_handler

# Read .ply file
cols = 3 
input_file = "/home/afz/Downloads/depoco/tmc_13/mpeg-pcc-tmc13/experiment/lossy-geom-no-attrs/longdress_viewdep_vox12/r01/longdress_viewdep_vox12.ply.bin.decoded.ply"
pcd = o3d.io.read_point_cloud(input_file) # Read the point cloud


# Visualize the point cloud within open3d
#o3d.visualization.draw_geometries = draw_geometries # replace function
o3d.visualization.draw_geometries([pcd]) 

# Convert open3d format to numpy array
# Here, you have the point cloud in numpy format. 
np_points = np_colors = np.asarray(pcd.points)
print("np points" , np_points)
np_colors = np.asarray(pcd.colors)
print("np colors", np_colors)

sparse_points_features = np.hstack((np_points, np_colors))

print("hstack", sparse_points_features)

points_ag = sparse_points_features[:, :3]
print("point ag",points_ag)

octree=octree_handler.Octree()
octree.setInput(points_ag)
eig_normals = octree.computeEigenvaluesNormal(1.25)

print("eig normals", eig_normals)

sparse_points_features=np.hstack(
    (sparse_points_features, eig_normals))



#pcd.colors = o3d.utility.Vector3dVector(rgb_t.astype(np.float) / 255.0)

#data = np.reshape(point_cloud_in_numpy, (cols, int(point_cloud_in_numpy.size/cols)))
#print ("###")
#print (data.T)
