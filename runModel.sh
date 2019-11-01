#/bin/bash 

if [ ! -n "$1" ]; then
    echo "num of videos is needed!"
    exit
fi
VIDEOS_NUMS=$1
ROOT_DIR=/seu_share/home/csqjxiao/hox/video-caption.pytorch
C3D_DIR=/seu_share/home/csqjxiao/hox/video-classification-3d-cnn-pytorch

echo "[INFO]Num of videos:$VIDEOS_NUMS" 

## feats
echo "[INFO]Now extrect feats:..."
cd $ROOT_DIR
python prepro_feats.py --output_dir data/feats/resnet152 --model resnet152 --n_frame_steps 40  --gpu 0
echo "[INFO]Now extrect 3d-feats:..."
cd $C3D_DIR
python main.py --input ./input --video_root ./videos --output ./output.json --model ./resnet-34-kinetics.pth --mode feature --num $VIDEOS_NUMS 2> /dev/null

## cd run
cd $ROOT_DIR
echo "[INFO]Now Run model and get captions:"
python useModel.py --recover_opt data/save/opt_info.json --saved_model data/save/model_900.pth --batch_size 1 --gpu 1 2>/dev/null

