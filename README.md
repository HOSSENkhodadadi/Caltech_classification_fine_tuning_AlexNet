# Caltech 101 Classification
## Description
This project implements a deep learning model for image classification on the Caltech 101 dataset. The model is trained using PyTorch and monitored using Weights & Biases (wandb).
## Project Structure
```bash
Caltech_classification_fine_tuning_AlexNet/
├── src/                          
│   ├── inference.py              
│   ├── preprocess.py             
│   ├── utils.py                  
│   └── config.py                 
├── models/                       
│   └── model_v1.pkl              
├── data/                         
│   └── schemas/                  
├── and tests/                        
│   └── test_inference.py         
├── api/                          
│   └── app.py                    
├── deployment/                   
│   ├── Dockerfile                
│   ├── docker-compose.yml        
│   ├── k8s/                      
│   └── helm/                     
├── monitoring/                   
│   ├── metrics.py                
│   └── alerts.py                 
├── .github/workflows/            
│   └── deploy.yml                
├── requirements.txt             
├── README.md                    , 
└── .env.example                  

```

## Installation
To run this project, you need to install the Weights & Biases library (wandb). You can install it via pip:<br/>
```bash
pip install wandb
```

You also need to clone the dataset repository inside the `data` folder. Run the following command in your terminal:<br/>
```bash
git clone https://github.com/MachineLearning2020/Homework2-Caltech101.git
```

## Usage
Once you have installed the required libraries and cloned the dataset repository, change the directory to the `src` folder,  you can use the following command-line arguments to customize the training process:

```bash
python caltech_101_kaggle_v4.py --epoch NUM_EPOCHS --batch_size BATCH_SIZE --lr LR --momentum MOMENTUM --weight_decay WEIGHT_DECAY --fine_tune_mode PRETRAINED --fine_tune_setting FINE_TUNE_SETTING
```

- `--epoch`: Number of epochs for training (default is 30).
- `--batch_size`: Batch size for training (default is 16).
- `--lr`: Learning rate (default is 0.001).
- `--momentum`: Momentum value (default is 0.9).
- `--weight_decay`: Weight decay (default is 1e-5).
- `--fine_tune_mode`: Boolean value indicating whether to use fine-tuning or not (default is True).
- `--fine_tune_setting`: Fine-tuning setting (default is "all").you may choose this parameter among `all`, `classifier` and `features`  

Note: You can omit any arguments to use their default values.

## Example
Here's an example command to start training:
```bash
python caltech_101_kaggle_v4.py --epoch 10 --batch_size 32 --lr 0.001 --momentum 0.9 --weight_decay 0.0001 --fine_tune_mode True --fine_tune_setting "setting_1"
```
This command will train the model for 10 epochs with a batch size of 32, learning rate of 0.001, momentum of 0.9, weight decay of 0.0001, using fine-tuning mode with setting "setting_1".
## Results
## Acknowledgments
- This project uses the Caltech 101 dataset.
- Weights & Biases (wandb) is used for experiment tracking and visualization.





<!-- Caltech_classification_fine_tuning_AlexNet/
├── src/                          # Core code for serving (reused from training src/)
│   ├── inference.py              # Model loading and prediction logic
│   ├── preprocess.py             # Lightweight data preprocessing for inputs
│   ├── utils.py                  # Helpers (e.g., logging, validation)
│   └── config.py                 # Runtime configs (e.g., model path, thresholds)
├── models/                       # Deployed model artifacts (from training, versioned)
│   └── model_v1.pkl              # Pickled model or ONNX/TensorFlow SavedModel
├── data/                         # Minimal—only schemas or sample inputs (no raw data)
│   └── schemas/                  # Input/output data validation schemas (e.g., Pydantic)
├── and tests/                        # Integration tests for serving
│   └── test_inference.py         # Tests for API endpoints
├── api/                          # Serving layer (e.g., REST API)
│   └── app.py                    # FastAPI/Flask app for predictions
├── deployment/                   # Deployment
│   ├── Dockerfile                # Containerize the app
│   ├── docker-compose.yml        # Local, testing with Docker
│   ├── k8s/                      # Kubernetes manifests (e.g., deployment.yaml)
│   └── helm/                     # Helm charts for cloud deployment
├── monitoring/                   # Production monitoring
│   ├── metrics.py                # Logging metrics (e.g., latency, accuracy drift)
│   └── alerts.py                 # Alerts for model
├── .github/workflows/            # CI/CD for deployment
│   └── deploy.yml                # Auto-deploy on merge
├── requirements.txt              # Dependencies (minimal, production-optimized)
├── README.md                    , # Deployment instructions
└── .env.example                  # Environment vars (e.g., MODEL_PATH) -->