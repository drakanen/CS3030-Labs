import logging

logging.basicConfig(filename='app.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

logging.info("Hello World!")
logging.warning("World, are you feeling okay?")
logging.error("World, you need to go to the ER right now!")