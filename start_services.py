import subprocess
import time

# Streamlit'i arka planda başlat
streamlit_process = subprocess.Popen(['streamlit', 'run', 'app.py', '--server.port', '8501'])

# Flask API'yi arka planda başlat
flask_process = subprocess.Popen(['python', 'api.py'])

try:
    while True:
        time.sleep(1)  # Sonsuz döngü ile script çalışmaya devam eder
except KeyboardInterrupt:
    streamlit_process.terminate()
    flask_process.terminate()

