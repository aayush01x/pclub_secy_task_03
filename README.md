# pclub_secy_task_03

I wasn't able to complete this task, just putting out what I did.

### Dataset
I used Masked ffhq dataset : https://github.com/cabani/MaskedFace-Net

But problem with this dataset is that it is not labelled according to gender, so I had to use another model which had classified images in ffhq dataset according to gender, https://github.com/DCGM/ffhq-features-dataset and then select random images ( ~7000 ) to train from the large dataset and retrieve their gender from json file according to label, seperate the into Male, Female.

Then firstly, I used VGG model with some extra layers, which didnt give a pretty good result.
Then, I thought of using Some other models like EfficientNet or MobileNet, but I didn't have much time.

I did try one interesting approach which was of FaceInPainting, approach was to inpaint face in place of mask, and then classify the image got as if person didn't wear mask. This would have produced very good results, but Faceinpainting try, failed miserabely as I wasn't able to get the job done.
