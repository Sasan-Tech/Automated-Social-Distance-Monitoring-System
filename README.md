# Intelligent-Systems

This repository was created for Project Assignment of COS30018 INTELLIGENT SYSTEMS in Swinburne Sarawak Semester 1, 2021.

Group Members:

1. Alesandro Michael Ferdinand (101228984)
2. Bryan Austyn Ichsan (101229576)
3. George Kennedy (101218969)

**Project**: Design and implementation of a simple machine learning system that could automatically detect persons and analyze the social distance between them.

**Modules involved**: Machine learning, Deep Learning, Person detection

# Background
Back in December 2019, there was an outbreak in the city of Wuhan, China that is caused by a virus called SARS-CoV-2. This type of Coronavirus has caused a pandemic level of respiratory illness throughout the world. According to WHO (World Health Organization) the cases of COVID-19 have been reported more than 160 million cases with more than 3 million deaths around the world in 20 May 2021.

WHO states people can take safety and simple precautions such as wearing a mask, avoiding big crowds, and doing the social distancing in order to protect ourselves from this contagious disease. Despite of all the methods, there is a problem that we have to address, which is in keeping track and ensuring the methods and measures are properly implemented in the society especially in ensuring people are adhering to the safe physical distance between people, which is 6 feet or approximately 2 meters. 

Thus, we are proposing a solution which aim to alleviate the problem in ensuring the protocols are implemented properly whereby we are developing an automated social distance monitoring system that has the capabilities to detect any violation in social distancing measures. We are using the deep learning object detection models for detecting people in combination with the algorithms for measuring the distance between people for detecting any violation in the social distancing protocol. Moreover, we are using three different models in expectation in figuring out on which model is the appropriate and effective in detecting people in our case.

Here is the snippet of real-time video detection:

![tempVideo](https://user-images.githubusercontent.com/71062416/119129194-2a5cf680-ba69-11eb-86b1-5bf594d52067.gif)

Please watch this demo video [here](https://www.youtube.com/watch?v=uit996L-Vus) to help you understand on how to use the user interface for running and utilizing the entire system. 

<!-- taken from introduction in the report, 1 - 2 lines only -->
<!-- show the result -->
<!-- tell them that the demo video is avaiable to guide them on how to use the GUI -->

# Folder Management

In order to train the models, we will need to set the Google Drive directory to store the data that we need to use in order to do the training. The path that we used in the colab file can be changed accordingly, but the path that we included here is the recommendation that we have used for our project. Please take note that all folders will be placed inside of the **SocialDistancing** folder in the root folder of Google Drive.

![image](https://user-images.githubusercontent.com/68536952/118913861-736f5680-b954-11eb-9b96-2ccedee3452d.png)

The folders above are specially created for Google Drive to trained and export the model. In order to run the GUI, we will need to follow the pattern of the directory that we have used for this project since we will work with python file from now onwards. You can easily pull the repository to see the arrangement of the folders in a better view.

# Prior preparation

Before we can start to train the model and run the program, we may need to prepare several things as stated below:

<ul>
 <li>Anaconda</li>
 <li>Python</li>
 <li>Tensorflow v1</li>
 <li>Required library, such as Matplotlib, CV2, PyQt5</li>
 <li>Google account</li>
 <li>Google Drive with at least 7.5GB free space</li>
 <li>Google Colaboratory</li>
</ul>

# Important Notes
- Please install **TensorFlow version 1** (Recommended - Version 1.5.0) packages and required libraries stated in [Prior preparation](#prior-preparation) above in your virtual environment and use the environment to run the **main.py** file. These are necessary so that the code can be successfully compiled.
- The duration of the video to be uploaded is suggested to be **5 seconds at max** since the video duration affects the detection & analysis process. More duration of video, more time to process.
- We provide a video for testing the system called **TownCentreXVID.mp4** in the repository just in case you need one.


# Steps

### 1. Prepare the dataset
Download the dataset that will be used for training the model [here](https://academictorrents.com/details/35e83806d9362a57be736f370c821960eb2f2a01)
### 2. Download the pre-trained model
Download the pre-trained model that you want to use [here](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md). In this project our team have used 3 models **(rfcn, ssd_mobilenet_v1_coco & ssd_inception)**

> Note: If the selected model cannot be downloaded directly, copy the link address and paste it on a new tab.

### 3. Create all the required folders in your Google Drive
By referring to the picture shown in [Folder Management](#folder-management), there are several things you need to pay attention to while creating the SocialDistancing folder in your Google Drive:

- Import files from the [dataset](https://academictorrents.com/details/35e83806d9362a57be736f370c821960eb2f2a01) that has been downloaded into this path **/Data**
- Import the downloaded [model](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md) folder into this path **/Models/pre-trained**
- Create a folder to store the trained model inside this path **/Models/trained**

  > Recommended name format: 'model name'\_'trained'. E.g. 'rfcn_trained'

- Create a folder to store the exported model inside this path **/Models/exported**
  > Recommended name format: 'model name'\_'exported'. E.g. 'rfcn_exported'

For the rest, just create the folders and files using the same name (Recommended) and follow the folder hierarchy shown in [Folder Management](#folder-management)
### 4. Run and follow the commands given inside the Google Colaboratory
In order to produce a model that can be used to automatically detect persons and analyze the social distance between them, you need follow the steps inside our Colaboratory. Click this link [here](https://colab.research.google.com/drive/1UJRB5T5CDHOTNQlGPTz2-0vh0zyZaiM6?usp=sharing) to open the Colaboratory or you might want to open it through **ASDTM.ipynb** file provided in this repository.

#### Follow below step immediately if you want to use the Automated Social Distancing Monitoring System right away by using the provided models or you have followed all the steps given in the Colaboratory & successfully produced your exported model:

### 5. Clone this repository (If you haven't done so) and run the system
#### Using the provided models (Recommended)
Clone this GitHub repository to your local directory and run the **main.py** file. Please watch this video [here](https://www.youtube.com/watch?v=uit996L-Vus) to help you understand on how to use the user interface for running and utilizing the entire system. 

#### Using your exported model
Clone this GitHub repository to your local directory and import your exported model from your Google Drive into the exported folder within the repository that you have cloned to your local directory. Next, before running the **main.py** file, you need to adjust your model path in **main.py**.
>Adjust here:
![image](https://user-images.githubusercontent.com/71062416/119104454-db09cc80-ba4e-11eb-9c73-9e34a75aa3fe.png)

>Note: You can do other adjustments on the GUI such as adding a new button for a new model, adjusting the button name with your model name & etc.
 

<!-- Download the model that they want to use, https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/tf1_detection_zoo.md -->
<!-- Make all the required folders in drive -->
<!-- Run the colab with appropriate command, ask them to follow the commands that have been provided in colab -->
<!-- Download the exported model from their drive into their own local directory (in the exported folder?) -->
<!-- Run the main.py -->







