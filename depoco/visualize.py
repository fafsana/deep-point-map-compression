import depoco.utils.point_cloud_utils as pcu
import argparse
import ruamel.yaml as yaml
from depoco.trainer import DepocoNetTrainer
import torch
import os ;
import gc;
import open3d as o3d

if __name__ == "__main__":
    print('Hello')
    os.environ['CUDA_LAUNCH_BLOCKING'] = '1';
    gc.collect()
    torch.cuda.empty_cache()
    
    parser = argparse.ArgumentParser("./sample_net_trainer.py")
    parser.add_argument(
        '--config', '-cfg',
        type=str,
        required=False,
        default='config/depoco.yaml',
        help='configitecture yaml cfg file. See /config/config for example',
    )
    parser.add_argument(
        '--number', '-n',
        type=int,
        default=1,
        help='Number of maps to visualize',
    )
    FLAGS, unparsed = parser.parse_known_args()

    FLAGS.config = "/home/afz/Downloads/depoco/deep-point-map-compression/depoco/config/longdress/e3.yaml"

    save_fname = '/home/afz/Downloads/depoco/deep-point-map-compression/depoco/experiments/recons/e3_000000_decode.ply'

    print('passed flags')
    config = yaml.safe_load(open(FLAGS.config, 'r'))
    print('loaded yaml flags')
    trainer = DepocoNetTrainer(config)
    trainer.loadModel(best=True)
    print('initialized  trainer')
    print(trainer.submaps.getOrderedTrainSet())

    for i, batch in enumerate(trainer.submaps.getOrderedTrainSet()):
        print('I am here')
        with torch.no_grad():
            points_est,nr_emb_points = trainer.encodeDecode(batch)
            print(
                f'nr embedding points: {nr_emb_points}, points out: {points_est.shape[0]}')
            
            recon_points = points_est.detach().cpu().numpy()
            pcu.visPointCloud(recon_points)
            recon_pcd = o3d.geometry.PointCloud()
            recon_pcd.points = o3d.utility.Vector3dVector(recon_points)
            o3d.io.write_point_cloud(save_fname, recon_pcd)
        if i+1 >= FLAGS.number:
            break
