# Log Generator
This is a simple log file generator that is used to generate a log file containing program installation information.

## How to use
This is a python based api endpoint using flask. To run the server make sure you have python installed. 

### Prerequisites
- Python 3.10
- Flask

### Installation

1. Clone the repo
   ```sh
   git clone 
    ```
2. Install flask
    ```sh
    pip install flask
    ```
3. Run the server
    ```sh
    python log_generator.py
    ```

## API Endpoints
* GET /generate_log: Accepts a Json object with a key of "logs". The value of of the key should be a list of lists. Each child list represents a log entry with the format of [<ProgramName>, <Status>, <Message>]. The endpoint will return a comma-separated values (.csv) file containing all the information in the request.
### Example
POST request to /log_generator
```
{
    "logs": [['Program1', 'Success', '<3'], ['Program2', 'Failure', ':(']]]
}
```
Response
* logfile_YYYYMMDD_HHMMSS.csv:

| Program  | Install Status | Message |
|:--------:|:--------------:|:-------:|
| Program1 |    Success     |   <3   |
| Program2 |    Failure     |   :(    |

