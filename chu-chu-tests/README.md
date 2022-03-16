To run the tests firstly:
1. Perform the installation of pytest and selenium via: 
pip install -r requirements.txt
2. Choose your driver (chromedriver) and put it in a "driver" folder of chu-chu-tests

Then just run tests with the command:
pytest chu-chu-tests/tests/test_user_acceptence.py

Variable '--host' could be used for definition of the app host. By default it's 'http://0.0.0.0:8000/'