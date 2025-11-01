from flask import Flask, render_template, request, send_file
from datetime import datetime, timedelta
from lunardate import LunarDate
from ics import Calendar, Event
import io

app = Flask(__name__)

def generate_ics(name, lunar_month, lunar_day, years, remind_days=3):
    cal = Calendar()
    current_year = datetime.now().year
    for y in range(current_year, current_year + years):
        try:
            solar_date = LunarDate(y, lunar_month, lunar_day).toSolarDate()
            event = Event()
            event.name = f"{name} 的农历生日"
            event.begin = solar_date
            event.make_all_day()
            event.description = f"{name} 的农历生日（农历 {lunar_month} 月 {lunar_day} 日）"

            # 提前提醒
            reminder_date = solar_date - timedelta(days=remind_days)
            event.alarms.append({
                "action": "display",
                "trigger": timedelta(days=-remind_days)
            })

            cal.events.add(event)
        except ValueError:
            continue

    output = io.StringIO(str(cal))
    return io.BytesIO(output.getvalue().encode('utf-8'))

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        lunar_date = request.form["lunar"]
        years = int(request.form["years"])
        month, day = map(int, lunar_date.split("-"))

        ics_file = generate_ics(name, month, day, years)
        filename = f"{name}_lunar_birthday.ics"

        return send_file(
            ics_file,
            as_attachment=True,
            download_name=filename,
            mimetype="text/calendar"
        )

    return render_template("index.html")

if __name__ == "__
