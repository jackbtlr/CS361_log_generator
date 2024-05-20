from flask import Flask, request, send_from_directory
from datetime import datetime
from pathlib import Path

app = Flask(__name__)
log_folder = "./log_files"

@app.route('/generate_log', methods=['POST'])
def generate_log_file():
    # create folder for log files if none exists
    Path(log_folder).mkdir(parents=True, exist_ok=True)

    # create timestamped log file
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f'{log_folder}/logfile_{timestamp}.csv'

    logs = request.json['logs']

    with open(filename, 'w') as file:
        file.write('Program,Install Status,Message\n')
        for i in range(len(logs)):
            file.write(f'{logs[i][0]},{logs[i][1]},{logs[i][2]}\n')

    resp = send_from_directory(
        log_folder, f'logfile_{timestamp}.csv', as_attachment=True
    )
    resp.headers['Filename'] = f'logfile_{timestamp}.csv'

    return resp

if __name__ == '__main__':
    app.run()