from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    df = pd.read_csv('strava_segments.csv')
    
    # Ambil 10 data pertama saja agar web tidak terlalu berat saat dimuat
    df_limit = df.head(10)
    
    # 2. Ubah data Excel menjadi tabel HTML murni
    # Kita tambahkan class Bootstrap 'table table-striped' agar tampilannya rapi nanti
    tabel_html = df_limit.to_html(classes='table table-striped table-hover', index=False)
    
    # 3. Kirim tabel HTML tersebut ke file index.html
    return render_template('index.html', tabel_dataset=tabel_html)

if __name__ == '__main__':
    app.run(debug=True)