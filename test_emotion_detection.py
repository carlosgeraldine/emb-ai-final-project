import unittest
import logging
from EmotionDetection import emotion_detector

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function"""
    
    def setUp(self):
        """Set up test case - runs before each test"""
        logger.info("Setting up test case")
    
    def tearDown(self):
        """Clean up after test case - runs after each test"""
        logger.info("Cleaning up after test case")
        logger.info("-" * 70)
    
    def test_joy(self):
        """Test joy detection"""
        logger.info("Testing joy emotion detection")
        test_text = "I am glad this happened"
        logger.info(f"Test text: {test_text}")
        
        result = emotion_detector(test_text)
        logger.info(f"Result: {result}")
        
        self.assertEqual(result['dominant_emotion'], 'joy')
        logger.info("Joy test completed successfully")
    
    def test_anger(self):
        """Test anger detection"""
        logger.info("Testing anger emotion detection")
        test_text = "I am really mad about this"
        logger.info(f"Test text: {test_text}")
        
        result = emotion_detector(test_text)
        logger.info(f"Result: {result}")
        
        self.assertEqual(result['dominant_emotion'], 'anger')
        logger.info("Anger test completed successfully")
    
    def test_disgust(self):
        """Test disgust detection"""
        logger.info("Testing disgust emotion detection")
        test_text = "I feel disgusted just hearing about this"
        logger.info(f"Test text: {test_text}")
        
        result = emotion_detector(test_text)
        logger.info(f"Result: {result}")
        
        self.assertEqual(result['dominant_emotion'], 'disgust')
        logger.info("Disgust test completed successfully")
    
    def test_sadness(self):
        """Test sadness detection"""
        logger.info("Testing sadness emotion detection")
        test_text = "I am so sad about this"
        logger.info(f"Test text: {test_text}")
        
        result = emotion_detector(test_text)
        logger.info(f"Result: {result}")
        
        self.assertEqual(result['dominant_emotion'], 'sadness')
        logger.info("Sadness test completed successfully")
    
    def test_fear(self):
        """Test fear detection"""
        logger.info("Testing fear emotion detection")
        test_text = "I am really afraid that this will happen"
        logger.info(f"Test text: {test_text}")
        
        result = emotion_detector(test_text)
        logger.info(f"Result: {result}")
        
        self.assertEqual(result['dominant_emotion'], 'fear')
        logger.info("Fear test completed successfully")

if __name__ == "__main__":
    # Create test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TestEmotionDetector)
    
    # Create test runner with verbosity=2 for detailed output
    runner = unittest.TextTestRunner(verbosity=2)
    
    logger.info("Starting Emotion Detection Tests")
    logger.info("=" * 70)
    
    # Run the tests
    result = runner.run(suite)
    
    logger.info("=" * 70)
    logger.info(f"Tests Run: {result.testsRun}")
    logger.info(f"Tests Failed: {len(result.failures)}")
    logger.info(f"Tests Errors: {len(result.errors)}")