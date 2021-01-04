import inspect
import logging
import time
import utilities.setup as st


# Path to store log files
LOGS_FOLDER = f"{st.get_root_test_dir()}/results/logs/"


def customLogger(logLevel=logging.DEBUG):

    """
        Logging mechanism to read the logs within the test execution.
        
        A new .log file is generated per execution, following the naming
            convention based on date-time
        
        Test Class names are fetched into the logs generated to make the logs readable
    """

    # Get the name of function / method where the information is logged
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)

    # Default setting: Log all the messages
    logger.setLevel(logging.DEBUG)

    # Define the filename for the logfile generated
    current_time = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
    log_file_name = LOGS_FOLDER+current_time+".log"

    # Generate the logfile
    fileHandler = logging.FileHandler(log_file_name, mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                  datefmt='%m/%d/%Y %I:%M:%S %p')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
