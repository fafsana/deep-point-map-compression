import numpy as np
import open3d as o3d
import octree_handler
import depoco.evaluation.evaluator as evaluator
from ruamel import yaml
import torch

r_name = "r08"
reconstruction_error_avg = 0 
config_cfg = "/home/afz/Downloads/depoco/deep-point-map-compression/depoco/config/longdress/e0.yaml"
config = yaml.safe_load(open( config_cfg , 'r'))
    
for i  in range(0,300):
    
    fname = str(i).zfill(6)

    recon_input_file = "/home/afz/Downloads/depoco/tmc_13/mpeg-pcc-tmc13/experiment/lossy-geom-no-attrs/longdress_viewdep_vox12/{}/{}.ply.bin.decoded.ply".format(r_name,fname)
    pcd_recon = o3d.io.read_point_cloud(recon_input_file) # Read the point cloud

    input_file = "/home/afz/Downloads/depoco/data/longdress/one_ply/{}.ply".format(fname)
    pcd = o3d.io.read_point_cloud(input_file) # Read the point cloud

    loss_evaluator = evaluator.Evaluator(config)


    # Visualize the point cloud within open3d
    #o3d.visualization.draw_geometries = draw_geometries # replace function
    #o3d.visualization.draw_geometries([pcd_recon]) 

    # Convert open3d format to numpy array
    # Here, you have the point cloud in numpy format. 
    #np_points = np_colors = np.asarray(pcd.points)
    #print("np points" , np_points)
    #np_colors = np.asarray(pcd.colors)
    #print("np colors", np_colors)

    #sparse_points_features = np.hstack((np_points, np_colors))

    #print("hstack", sparse_points_features)

    #points_ag = sparse_points_features[:, :3]
    #print("point ag",points_ag)

    #octree=octree_handler.Octree()
    #octree.setInput(points_ag)
    #eig_normals = octree.computeEigenvaluesNormal(1.25)

    #print("eig normals", eig_normals)

    #sparse_points_features=np.hstack( (sparse_points_features, eig_normals))

    #print("sparse_points_features", sparse_points_features.shape)

    #print("pcd_recon" , np.asarray(pcd_recon.points).shape)

    #print("pcd " , np.asarray(pcd.points).shape)

    #print("eig noraml " , eig_normals.shape)

    reconstruction_error = loss_evaluator.chamferDist(
                        gt_points= torch.tensor(np.asarray(pcd_recon.points ),dtype=torch.float32), 
                        source_points= torch.tensor(np.asarray(pcd.points),dtype=torch.float32))
                        #gt_normals=torch.tensor(np.asarray(eig_normals),dtype=torch.float32))
                    
    reconstruction_error_avg += reconstruction_error 

    print(reconstruction_error)

print(reconstruction_error_avg/300)

#pcd.colors = o3d.utility.Vector3dVector(rgb_t.astype(np.float) / 255.0)

#data = np.reshape(point_cloud_in_numpy, (cols, int(point_cloud_in_numpy.size/cols)))
#print ("###")
#print (data.T)
