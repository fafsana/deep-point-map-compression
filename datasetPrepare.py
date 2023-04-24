import numpy as np
import plotly.graph_objects as go
import os
import open3d as o3d
import octree_handler

def saveCloud2Binary(cld, colors , eig_normals, file, out_path=None):
    if out_path is None:
        out_path = ''
    else:
        if not os.path.exists(out_path):
            os.makedirs(out_path)
    f = open(out_path+file, "wb")
    #print("cld --> ")
    #print( cld)
    sparse_points_features=np.hstack(
    (cld, colors,eig_normals))

    #f.write(cld.astype('float32').T.tobytes())
    f.write(sparse_points_features.astype('float32').T.tobytes())
    f.close()

def loadCloudFromBinaryPly(file, cols=3):
    print (file)
    pcd = o3d.io.read_point_cloud(file) # Read the point cloud
    #temp = np.asarray(pcd.points)
    #data = np.reshape(temp, (cols, int(temp.size/cols)))
    return pcd

fnames = ["00_000002",
          "00_000018",
          "00_000039",
          "00_000065",
          "00_000081",
          "01_000010",
          "01_000055",
          "01_000061",
          "01_000075",
          "01_000089",
          "02_000016",
          "02_000034",
          "02_000048",
          "02_000060",
          "02_000078",
          "02_000099"]


normal_eigenvalue_radius = 1.25

for fname in fnames:
  print (fname)

#for i  in range(0,100):
#  fname = str(i).zfill(6)
  
  file_path = '/content/longdress_subsample/longdress_subsample/validation_ply/'+fname+'.ply' 
  out_file_path = "/content/longdress_subsample/longdress_subsample/validation/"
  #file_path = '/content/longdress_subsample/longdress_subsample/02_ply/'+fname+'.ply' 
  #+ str(i).zfill(6) + '.ply'
  #out_file_path = "/content/longdress_subsample/longdress_subsample/02/"
  file_name = fname+".bin"#str(i).zfill(6) + ".bin"
  pcd = loadCloudFromBinaryPly(file_path)
  #print("points -> ")
  #print(pcd.points)
  
  #print("colors  -> ")
  #print(pcd.colors)
  octree=octree_handler.Octree()
  octree.setInput(np.asarray(pcd.points))
  eig_normals = octree.computeEigenvaluesNormal(normal_eigenvalue_radius)
  
  saveCloud2Binary(np.asarray(pcd.points),np.asarray(pcd.colors),eig_normals,file_name,out_file_path)


#for fname in fnames:
#  print (fname)

for i  in range(0,100):
  fname = str(i).zfill(6)
  
#  file_path = '/content/longdress_subsample/longdress_subsample/validation_ply/'+fname+'.ply' 
#  out_file_path = "/content/longdress_subsample/longdress_subsample/validation/"
  file_path = '/content/longdress_subsample/longdress_subsample/00_ply/'+fname+'.ply' 
  #+ str(i).zfill(6) + '.ply'
  out_file_path = "/content/longdress_subsample/longdress_subsample/00/"
  file_name = fname+".bin"#str(i).zfill(6) + ".bin"
  pcd = loadCloudFromBinaryPly(file_path)
  #print("points -> ")
  #print(points)
  octree=octree_handler.Octree()
  octree.setInput(np.asarray(pcd.points))
  eig_normals = octree.computeEigenvaluesNormal(normal_eigenvalue_radius)
  
  saveCloud2Binary(np.asarray(pcd.points),np.asarray(pcd.colors),eig_normals,file_name,out_file_path)



for i  in range(0,100):
  fname = str(i).zfill(6)
  
#  file_path = '/content/longdress_subsample/longdress_subsample/validation_ply/'+fname+'.ply' 
#  out_file_path = "/content/longdress_subsample/longdress_subsample/validation/"
  file_path = '/content/longdress_subsample/longdress_subsample/01_ply/'+fname+'.ply' 
  #+ str(i).zfill(6) + '.ply'
  out_file_path = "/content/longdress_subsample/longdress_subsample/01/"
  file_name = fname+".bin"#str(i).zfill(6) + ".bin"
  pcd = loadCloudFromBinaryPly(file_path)
  #print("points -> ")
  #print(points)
  octree=octree_handler.Octree()
  octree.setInput(np.asarray(pcd.points))
  eig_normals = octree.computeEigenvaluesNormal(normal_eigenvalue_radius)
  
  saveCloud2Binary(np.asarray(pcd.points),np.asarray(pcd.colors),eig_normals,file_name,out_file_path)

for i  in range(0,100):
  fname = str(i).zfill(6)
  
#  file_path = '/content/longdress_subsample/longdress_subsample/validation_ply/'+fname+'.ply' 
#  out_file_path = "/content/longdress_subsample/longdress_subsample/validation/"
  file_path = '/content/longdress_subsample/longdress_subsample/02_ply/'+fname+'.ply' 
  #+ str(i).zfill(6) + '.ply'
  out_file_path = "/content/longdress_subsample/longdress_subsample/02/"
  file_name = fname+".bin"#str(i).zfill(6) + ".bin"
  pcd = loadCloudFromBinaryPly(file_path)
  #print("points -> ")
  #print(points)
  octree=octree_handler.Octree()
  octree.setInput(np.asarray(pcd.points))
  eig_normals = octree.computeEigenvaluesNormal(normal_eigenvalue_radius)
  
  saveCloud2Binary(np.asarray(pcd.points),np.asarray(pcd.colors),eig_normals,file_name,out_file_path)
