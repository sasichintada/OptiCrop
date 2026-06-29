from flask import Flask, render_template, request
import pickle
import numpy as np
import traceback
import os

app = Flask(__name__)

# ============================================
# LOAD MODEL - WITH CORRECT PATHS
# ============================================

print("="*60)
print("🌾 OPTICROP - LOADING MODEL")
print("="*60)

# Get the directory where this file is located
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Try multiple possible paths for Render deployment
possible_model_paths = [
    os.path.join(BASE_DIR, '..', 'Model', 'models', 'crop_model.pkl'),
    os.path.join(BASE_DIR, 'Model', 'models', 'crop_model.pkl'),
    os.path.join(os.path.dirname(BASE_DIR), 'Model', 'models', 'crop_model.pkl'),
    'Model/models/crop_model.pkl',
]

possible_scaler_paths = [
    os.path.join(BASE_DIR, '..', 'Model', 'models', 'scaler.pkl'),
    os.path.join(BASE_DIR, 'Model', 'models', 'scaler.pkl'),
    os.path.join(os.path.dirname(BASE_DIR), 'Model', 'models', 'scaler.pkl'),
    'Model/models/scaler.pkl',
]

model = None
scaler = None

for model_path in possible_model_paths:
    for scaler_path in possible_scaler_paths:
        try:
            with open(model_path, 'rb') as f:
                model = pickle.load(f)
            with open(scaler_path, 'rb') as f:
                scaler = pickle.load(f)
            print(f"✅ Model and scaler loaded successfully!")
            print(f"📊 Model type: {type(model).__name__}")
            print(f"🌾 Number of crops: {len(model.classes_)}")
            print(f"📁 Model path: {model_path}")
            break
        except:
            continue
    if model is not None:
        break

if model is None or scaler is None:
    print("❌ Could not load model files!")
    print("⚠️ Please make sure crop_model.pkl and scaler.pkl exist in Model/models/")

print("="*60)


# ============================================
# ROUTES - PAGES
# ============================================

@app.route('/')
def home():
    return render_template('index.html', active_page='home')


@app.route('/features')
def features():
    return render_template('features.html', active_page='features')


@app.route('/recommendation')
def recommendation():
    return render_template('recommendation.html', active_page='recommendation')


@app.route('/about')
def about():
    return render_template('about.html', active_page='about')


@app.route('/contact')
def contact():
    return render_template('contact.html', active_page='contact')


# ============================================
# ROUTE - PREDICTION
# ============================================

@app.route('/predict', methods=['POST'])
def predict():
    # Check if model is loaded
    if model is None or scaler is None:
        return render_template('result.html', 
                             error="❌ Model not loaded. Please contact support.", 
                             active_page='recommendation')
    
    try:
        # Get form data
        print("📥 Form data received:", request.form)
        
        # Extract values
        try:
            N = float(request.form.get('nitrogen', 0))
            P = float(request.form.get('phosphorous', 0))
            K = float(request.form.get('potassium', 0))
            temp = float(request.form.get('temperature', 0))
            humidity = float(request.form.get('humidity', 0))
            ph = float(request.form.get('ph', 0))
            rainfall = float(request.form.get('rainfall', 0))
        except ValueError as e:
            return render_template('result.html', 
                                 error=f"❌ Invalid input: Please enter valid numbers. {str(e)}", 
                                 active_page='recommendation')
        
        # Validate inputs
        if N < 0 or P < 0 or K < 0:
            return render_template('result.html', 
                                 error="❌ Nutrient values (N, P, K) cannot be negative.", 
                                 active_page='recommendation')
        
        if temp < -50 or temp > 60:
            return render_template('result.html', 
                                 error="❌ Temperature seems unrealistic. Please enter a valid value.", 
                                 active_page='recommendation')
        
        # Prepare features
        features = np.array([[N, P, K, temp, humidity, ph, rainfall]])
        features_scaled = scaler.transform(features)
        
        # Make prediction
        prediction = model.predict(features_scaled)[0]
        confidence = model.predict_proba(features_scaled).max() * 100
        
        # Get top 3 predictions
        proba = model.predict_proba(features_scaled)[0]
        top_3_idx = np.argsort(proba)[-3:][::-1]
        top_3 = []
        for i in top_3_idx:
            crop_name = model.classes_[i]
            percentage = float(proba[i] * 100)
            top_3.append([crop_name, percentage])
        
        # Debug print
        print(f"✅ Prediction: {prediction} with {confidence:.1f}% confidence")
        print(f"📊 Top 3: {top_3}")
        
        # Render results
        return render_template('result.html',
                             crop=prediction,
                             confidence=f"{confidence:.1f}",
                             N=N, P=P, K=K,
                             temp=temp,
                             humidity=humidity,
                             ph=ph,
                             rainfall=rainfall,
                             top_3=top_3,
                             active_page='recommendation')
    
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        print(traceback.format_exc())
        return render_template('result.html', 
                             error=f"❌ An error occurred: {str(e)}", 
                             active_page='recommendation')


# ============================================
# ERROR HANDLERS
# ============================================

@app.errorhandler(400)
def bad_request(e):
    return render_template('result.html', 
                         error="❌ Bad Request: Please check your input values and try again.", 
                         active_page='home'), 400


@app.errorhandler(404)
def page_not_found(e):
    return render_template('result.html', 
                         error="❌ Page not found! Please check the URL.", 
                         active_page='home'), 404


@app.errorhandler(405)
def method_not_allowed(e):
    return render_template('result.html', 
                         error="❌ Method not allowed. Please use the form correctly.", 
                         active_page='home'), 405


@app.errorhandler(500)
def internal_error(e):
    return render_template('result.html', 
                         error="❌ Internal server error. Please try again later.", 
                         active_page='home'), 500


# ============================================
# RUN THE APP - UPDATED FOR RENDER
# ============================================

if __name__ == '__main__':
    print("\n" + "="*60)
    print("🚀 OPTICROP - STARTING APPLICATION")
    print("="*60)
    print("🌐 Open your browser and go to: http://127.0.0.1:5000")
    print("📱 Press CTRL+C to stop the server")
    print("="*60 + "\n")
    
    # Get port from environment variable (Render provides this)
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(debug=debug, host='0.0.0.0', port=port)
