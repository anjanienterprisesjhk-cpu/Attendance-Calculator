from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    percentage = None
    can_miss = None

    if request.method == "POST":
        attended = int(request.form["attended"])
        total = int(request.form["total"])

        if total > 0:
            percentage = round((attended / total) * 100, 2)

            target = 75

            if percentage >= target:
                future_total = total
                future_attended = attended

                while (future_attended / future_total) * 100 >= target:
                    future_total += 1

                can_miss = future_total - total - 1

    return render_template(
        "index.html",
        percentage=percentage,
        can_miss=can_miss
    )

if __name__ == "__main__":
    app.run(debug=True)