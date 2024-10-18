# Single Domain Generalization for Crowd Counting : MPCOUNT

## Requirements
* Python 3.10.12
* PyTorch 2.0.1
* Torchvision 0.15.2
* Others specified in [requirements.txt](requirements.txt)

## Data Preparation
1. Download [ShanghaiTech](https://www.kaggle.com/datasets/tthien/shanghaitech) and [UCF-QNRF](https://www.crcv.ucf.edu/data/ucf-qnrf/) datasets from hyper-link provided and unzip them.

2. Add above datasets in datasets/ 

3. To preprocess the datasets: ( it will update in data/ )
    1. open utils/preprocess_data.py
    2. update below in main function and run the file:
       ```
        origin_dir='datasets/ShanghaiTech/part_A'
        save_dir='data/sta/'
        min_size=512
        max_size=2048
        dataset='sta'
       ```
    3. update below in main function and run the file:
       ```
        origin_dir='datasets/ShanghaiTech/part_B'
        save_dir='data/stb/'
        min_size=512
        max_size=2048
        dataset='stb'    
       ```
    4. update below in main function and run the file: ( This might take some time )
       ```
        origin_dir='datasets/UCF-QNRF_ECCV18'
        save_dir='data/qnrf/'
        min_size=512
        max_size=2048
        dataset='qnrf'
       ```  
    

4. Run the following commands to generate GT density maps:
    ```
    python utils/dmap_gen.py --path data/sta
    python utils/dmap_gen.py --path data/stb
    python utils/dmap_gen.py --path data/qnrf
    ```

## Training
Run the following command for training on sta dataset:
```
python main.py --task train --config configs/sta_train.yml
```
You may edit the `.yml` config file as you like. (stb_train.yml or qnrf_train.yml )

## Best Weights - ( Use them for testing purpose )
link : https://drive.google.com/drive/folders/1yMUjVwtzTYGlbcb4omP5T3BA-DpO-5XZ?usp=sharing

## Testing ( Best weights provided above )
 + path to sta model weight: logs/sta/best.pth
 + path to stb model weight: logs/stb/best.pth
 + path to qnrf model weight: logs/qnrf/best.pth
   
Run the following commands after you specify the path to the model weight in the config file:

```
python main.py --task test --config configs/sta_test_stb.yml
```
Now you can change the '.yml' config file depending upon what testing you want to perform. All config files avaialbe in configs/ .

## Inference
Run the following command to get prediction of count of people and density map estimate for any image:
```
python inference.py --img_path [path_to_img_file_or_directory] --model_path [path_to_model_weight] --save_path output.txt --vis_dir vis
```
example: 
 ```
python inference.py --img_path datasets\ShanghaiTech\part_B\test_data\images\IMG_7.jpg --model_path logs\sta\best.pth --save_path output.txt --vis_dir vis

```
you will get results in vis/  

I have also added a python file to visualize Grount Truth density map: file: data/visualize_density_GT.py
Update the sources of the image (sample added in code)

## Project Report
[Project Report](Aayush_Gupta_210020_report.pdf) uploaded

## Citation
```
@inproceedings{pengMPCount2024,
  title = {Single Domain Generalization for Crowd Counting},
  booktitle = {Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR 2024)},
  author = {Peng, Zhuoxuan and Chan, S.-H. Gary},
  year = {2024}
}
```
