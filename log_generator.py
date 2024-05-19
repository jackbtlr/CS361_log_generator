from flask import Flask, request, send_from_directory
from datetime import datetime

app = Flask(__name__)

@app.route('/generate_log')
def generate_log_file():
    # create timestamped log file
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    filename = f'./log_files/logfile_{timestamp}.csv'


    log_info = request.json
    programs = log_info['programs']
    status = log_info['status']
    message = log_info['message']

    with open(filename, 'w') as file:
        file.write('Program,Install Status,Message\n')
        for i in range(len(programs)):
            file.write(f'{programs[i]},{status[i]},{message[i]}\n')
    return send_from_directory(
        './log_files', f'logfile_{timestamp}.csv', as_attachment=True
    )

if __name__ == '__main__':
    app.run()