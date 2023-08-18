# Diabetes Predictor for Women

This project aims to predict the likelihood of diabetes in women based on various health parameters. It utilizes a machine learning model trained on a dataset of women's health records. The model predicts whether a woman is likely to have diabetes or not, providing valuable insights for early detection and prevention.

## Software and Tools

1. [GitHub Account](https://github.com): Version control platform to host and manage your project code.
2. [VSCode IDE](https://code.visualstudio.com/download): Integrated development environment for coding and editing project files.
3. [Git CLI](https://git-scm.com/downloads): Command-line interface to interact with Git and manage version control.

## Setting up the Environment

To create a new environment for the project, run the following command in your command-line interface:

```
conda create -p diabetes python=3.9 -y
```


This command creates a new Python environment named "diabetes" with Python version 3.9.

## Running the Application

To start the application, use the following command:

```
waitress-serve --port $PORT app:app
```


This command starts the Waitress server and runs the Flask application on the specified port.

## Accessing the Deployed Application

The Diabetes Predictor for Women is deployed and accessible at [https://diabetes-pred-tbj3.onrender.com/](https://diabetes-pred-tbj3.onrender.com/). Visit the link to access the application and make predictions based on the provided health parameters.

Please note that this application is for educational and demonstration purposes only. It is not intended to replace professional medical advice. If you have concerns about your health, consult a healthcare professional.

## Repository Structure

The repository contains the following files:

- `app.py`: Python script that defines the Flask application and handles the prediction logic.
- `clmodel.pkl`: Pickle file containing the trained machine learning model for diabetes prediction.
- `requirements.txt`: Text file listing the required Python packages and their versions.

Feel free to explore the repository and modify the code as needed for your own projects.

## Contributing

If you would like to contribute to the project, please fork the repository, make your changes, and submit a pull request. Your contributions are greatly appreciated!

## License

The project is licensed under the [Apache-2.0 Licence](LICENSE). Please review the license file for more information.
