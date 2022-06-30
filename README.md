# K-Means-Clustering
K-Means Clustering (data science) project, for analyzing countries dataset.

### system startup:
To run the system, open the project folder in cmd and type:
###
     python GUI.py
    
### example run and workflow:    
When running the program, the main window will pop up:
<br>
![image](https://user-images.githubusercontent.com/62337691/176592477-a44960d7-82d2-459d-97e4-09d4ce52b842.png)
<br><br>
Click "Browse" to load the dataset file - only xlsx files can be loaded. A window will open where we will need to select the file:
<br>
![image](https://user-images.githubusercontent.com/62337691/176592558-f6162a5d-8356-4612-b4d6-394d9fe889c4.png)
<br><br>

After selecting the file, we can see that the text box "Choose path" contains the path of the file:
<br>
![image](https://user-images.githubusercontent.com/62337691/176592642-b2c235b3-7ccc-4596-b9a1-e47278e1c307.png)
<br><br>
Enter the desired values in the text boxes "Number of clusters k" and "Number of runs" (these values can be entered before or after performing the preprocessing):
<br>
![image](https://user-images.githubusercontent.com/62337691/176592727-8acc4cd4-48bc-4376-ad89-510fb76e7df9.png)
<br><br>
Click the "Pre-process" button. If the process is performed correctly, we will receive an appropriate indication:
<br>
![image](https://user-images.githubusercontent.com/62337691/176592767-d8d3ebe6-b0fd-4937-9dec-c1ce48a1ebd7.png)
<br><br>
Press "OK" button.
<br><br>
Press "Cluster" button, and the clustering process will be calculated and shown:
<br>
![image](https://user-images.githubusercontent.com/62337691/176592904-2ea4e0d4-6b4a-4d9d-ba4e-3705405e04fb.png)
<br><br>
An Excel file containing the dataframe output after performing data preprocessing step, which also includes the K-Means algorithm output for each country (the "cluster" column), will be saved in the project folder, under the name: "dataset_with_cluster.xlsx".

