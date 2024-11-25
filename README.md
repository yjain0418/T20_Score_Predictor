# 🏏 T20 Cricket Score Predictor  

Predict the final score of a T20 cricket match using machine learning! This project leverages the power of the XGBoost algorithm to estimate scores based on match conditions and recent performance metrics.


## 🌟 Features  
- Predict the final score based on:  
  - 🏟️ Teams involved  
  - 🌆 Match location (city)  
  - 📈 Current score  
  - ⏳ Overs completed  
  - ❌ Wickets down  
  - 🔥 Runs scored in the last 5 overs  
- Interactive interface for input and results display.  
- Deployed on **Streamlit Cloud** for easy access.


## 📂 Dataset  
The dataset used for this project is sourced from **[Kaggle's Cricsheet - A Retrosheet for Cricket](https://www.kaggle.com/datasets/veeralakrishna/cricsheet-a-retrosheet-for-cricket)**. It contains detailed match data, allowing comprehensive feature engineering and training.


## 🛠️ Tech Stack  
- **Machine Learning Algorithm:** XGBoost  
- **Libraries:**  
  - scikit-learn  
  - Streamlit  
  - Pickle  
  - YAML  
  - tqdm  
  - XGBoost  
  - Pipeline  


## 🏗️ Workflow  
1. **Data Extraction:** Gathered match data from Kaggle.  
2. **Feature Engineering:** Processed data to create meaningful input features.  
3. **Model Training:** Trained the machine learning model using XGBoost.  
4. **Deployment:** Deployed the application on Streamlit Cloud for user interaction.  


## 🚀 How to Use  
1. Visit the deployed application: [T20 Cricket Score Predictor](https://t20scorepredictor-yjain0418.streamlit.app/).  
2. Enter the match details like teams, city, current score, overs, wickets, and last five overs' score.  
3. Click "Predict" to see the estimated final score.  


## 📦 Installation (Local Setup)  
To run the project locally, follow these steps:  

1. Clone the repository:  
   ```bash
   git clone https://github.com/yjain0418/T20_Score_Predictor.git
   cd T20_Score_Predictor

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt

3. Run the Streamlit application:
    ```bash
    streamlit run app.py

## 🤝 Contributing
Contributions are welcome! Feel free to open issues or submit pull requests to improve the project.

## 📬 Contact
If you have any questions or feedback, reach out to me on [LinkedIn](www.linkedin.com/in/yjain0418).

## 🎯 Future Enhancements
- Include additional features like weather conditions and pitch type.
- Explore other ML models for better performance.
- Enhance the UI for an improved user experience.

Star ⭐ this repository if you found it useful! Happy Predicting! 🏏