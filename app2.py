from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
  command = ""
  action_type = "find_error"
  input1 = ""
  input2 = ""

  if request.method == "POST":
    action_type = request.form.get("action_type", "find_error")
    input1 = request.form.get("input1", "").strip()
    input2 = request.form.get("input2", "").strip()

    if action_type == "find_error":
      keyword = input2 if input2 else "error"
      command = f'Select-String -Path "{input1}" -Pattern "{keyword}"'
    elif action_type == "find_file":
      path = input1 if input1 else "."
      pattern = input2 if input2 else "*"
      command = f'Get-ChildItem -Path "{path}" -Filter "{pattern}" -Recurse'
    elif action_type == "copy_file":
      command = f'Copy-Item -Path "{input1}" -Destination "{input2}"'

  return render_template(
      "index2.html",
      command=command,
      action_type=action_type,
      input1=input1,
      input2=input2,
  )


if __name__ == "__main__":
  app.run(debug=True, port=5000)