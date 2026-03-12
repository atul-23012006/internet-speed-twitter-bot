import pandas as pd
import matplotlib.pyplot as plt
from flask import Flask, render_template
import os
app = Flask(__name__)

@app.route("/")
def index():
    if os.path.getsize("speed_log.csv") == 0:
        return "No speed data yet. Run main.py first."

    data = pd.read_csv("speed_log.csv", header=None)
    data.columns = ["date", "time", "download", "upload"]

    data["datetime"] = pd.to_datetime(data["date"] + " " + data["time"])

    plt.figure()

    plt.plot(data["datetime"], data["download"], label="Download Speed")
    plt.plot(data["datetime"], data["upload"], label="Upload Speed")

    plt.xlabel("Time")
    plt.ylabel("Speed (Mbps)")
    plt.title("Internet Speed History")
    plt.legend()

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.savefig("static/speed_graph.png")
    plt.close()

    avg_download = round(data["download"].mean(), 2)
    avg_upload = round(data["upload"].mean(), 2)

    return render_template(
        "index.html",
        avg_download=avg_download,
        avg_upload=avg_upload
    )


if __name__ == "__main__":
    app.run(debug=True)