import pytest
import time
import RPi.GPIO as GPIO

@pytest.fixture(scope="function")
def setup_gpio():
    """Setup and teardown for GPIO testing."""
    # Set the pin numbering mode (also set in each test for safety)
    GPIO.setwarnings(False)  # Disable warnings about channels in use
    try:
        GPIO.setmode(GPIO.BCM)
    except:
        # If already set, this might throw an error - ignore it
        pass
    
    # GPIO 17 will be set as an input to read LED state
    GPIO.setup(17, GPIO.IN)
    # GPIO 27 will be set as an output to emulate button presses
    GPIO.setup(27, GPIO.OUT, initial=GPIO.HIGH)  # Start HIGH (button not pressed)
    
    # GPIO 22 will be used as reset pin (connected to NRST)
    GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
    
    # Reset the system before each test
    GPIO.output(22, GPIO.LOW)  # Assert reset
    time.sleep(0.5)  # Hold reset for 0.5 seconds
    GPIO.output(22, GPIO.HIGH)  # Release reset
    time.sleep(0.5)  # Wait for system to initialize
    
    yield
    
    # Clean up GPIO settings after tests
    GPIO.cleanup()