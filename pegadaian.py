from flask import Flask, Response, jsonify
import requests
from bs4 import BeautifulSoup
import re

app = Flask(__name__)

def get_pegadaian_price():
    url = "https://digital.pegadaian.co.id/"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")

    harga_beli_div = soup.select_one("div.detail-harga__left h5")
    harga_jual_div = soup.select_one("div.detail-harga__right h5")

    harga_beli = harga_beli_div.get_text(strip=True) if harga_beli_div else None
    harga_jual = harga_jual_div.get_text(strip=True) if harga_jual_div else None

    def clean_number(text):
        if not text:
            return None
        match = re.search(r"Rp\s*([\d\.]+)", text)
        if match:
            return int(match.group(1).replace(".", ""))
        return None

    return clean_number(harga_beli), clean_number(harga_jual)


@app.route("/metrics")
def metrics():
    try:
        harga_beli, harga_jual = get_pegadaian_price()
        output = []
        output.append(f"# HELP pegadaian_harga_beli Harga beli emas Pegadaian (per 0.01 gr)")
        output.append(f"# TYPE pegadaian_harga_beli gauge")
        output.append(f"pegadaian_harga_beli {harga_beli}")

        output.append(f"# HELP pegadaian_harga_jual Harga jual emas Pegadaian (per 0.01 gr)")
        output.append(f"# TYPE pegadaian_harga_jual gauge")
        output.append(f"pegadaian_harga_jual {harga_jual}")

        return Response("\n".join(output), mimetype="text/plain")

    except Exception as e:
        return Response(f"# ERROR {e}", mimetype="text/plain"), 500


@app.route("/json")
def json_metrics():
    try:
        harga_beli, harga_jual = get_pegadaian_price()
        data = {
            "harga_beli": harga_beli,
            "harga_jual": harga_jual
        }
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
