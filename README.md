# 📌 Pegadaian Gold Price Scraper  

Program ini adalah **Python web server** yang melakukan scraping harga emas dari [Pegadaian Digital](https://digital.pegadaian.co.id/).  
Data hasil scrape tersedia dalam format **JSON** dan **Prometheus metrics**.  

---

## ⚡ Fitur
- Scraping otomatis harga **Beli** dan **Jual** emas dari situs Pegadaian.  
- Update data setiap **1 menit**.  
- Endpoint **JSON** untuk aplikasi/web lain.  
- Endpoint **/metrics** untuk integrasi Prometheus.  

---

## 🔧 Persyaratan
- Python 3.8 atau lebih baru  
- Pip (Python package manager)  

---

## 📦 Instalasi
1. Clone repository:
2. git clone https://github.com/username/pega-scrape.git
3. cd pega-scrape
4. pip install -r requirements.txt
5. python scraper.py

Secara default, web server berjalan di:
http://127.0.0.1:8000/metrics atau http://127.0.0.1:8000/json
