# Getting Started
Follow these steps to get the project up and running on your local machine.

## 1. Clone the Repository
Clone this repository to your local machine using the following command:

```
git clone https://github.com/  #will add later
```

## 2. Create a Virtual Environment
We recommend using Conda to create a virtual environment for this project. Navigate to the project directory and run the following command to create a Conda environment:

```
conda create --name house-env -y
```

Activate the virtual environment:
```
conda activate house-env
```


## 3. Install Requirements
Install the required Python packages by running the following command:

```
pip install -r requirements.txt
```

## 4. Train the Model
Run the notebook which will automatically save the model pickle file in the current directory, Make sure to select the kernel as our above created virtual enviroment from the top right corner of vs code window.


## 5. Run the Web App
I have developed a Streamlit-based web application for making house price predictions. To run the app, go to the parent folder and use the following command:

```
streamlit run house_prediction_app.py
```

Once the Streamlit app is running, you can input house information, and the app will provide a price prediction. 

## Contributing
If you would like to contribute to this project, please feel free to work on it.

## License
> This project is licensed under the `MIT License`. See the LICENSE file for details.
