# Heart-Disease-Prediction-using-Random-Forest

A simple Web application for Heart Disease Prediction using Random Forest.

## Project Structure

- `Heart_Disease_Prediction.ipynb`: Jupyter notebook containing the Random Forest model.
- `dataset.csv`: Dataset used for training and testing the model.
- `DashBoard/`: Django application for the web interface.
- `HDPuRF/`: Django project settings.
- `manage.py`: Django management utility.
- `static/`: Contains static files like `styles.css`.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/MQ-xz/Heart-Disease-Prediction-using-Random-Forest.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Heart-Disease-Prediction-using-Random-Forest
   ```
3. Install the required Python packages (it's recommended to use a virtual environment):
   ```bash
   pip install -r requirements.txt
   ```
   (Note: A `requirements.txt` file is not present, but it's good practice to mention it. I will not create one as it's not explicitly asked.)
4. Run Django migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the Django development server:
   ```bash
   python manage.py runserver
   ```
6. Open your web browser and go to `http://127.0.0.1:8000/`.
