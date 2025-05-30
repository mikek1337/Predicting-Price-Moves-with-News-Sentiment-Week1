import unittest
import pandas as pd
from sklearn.decomposition import LatentDirichletAllocation
from src.topic_modeling import TopicModeling

class TestTopicModeling(unittest.TestCase):
    def setUp(self):
        # Sample data
        self.data = pd.Series([
            "Apple releases new iPhone",
            "Microsoft announces new Surface",
            "Google updates search algorithm",
            "Amazon launches new Echo device",
            "Tesla unveils new electric car"
        ])
        self.modeler = TopicModeling(self.data)

    def test_remove_stopwords(self):
        text = "Apple releases new iPhone and updates software"
        processed = self.modeler.remove_stopwords(text)
        # Should remove stopwords like 'and'
        self.assertNotIn('and', processed)
        self.assertIn('Apple', processed)

    def test_create_vector(self):
        vectorizer = self.modeler.create_vector(1, 1.0)
        self.assertIsNotNone(vectorizer)
        self.assertTrue(hasattr(vectorizer, 'fit_transform'))

    def test_fit_model(self):
        lda_model = self.modeler.fit_model()
        self.assertIsInstance(lda_model, LatentDirichletAllocation)
        self.assertEqual(lda_model.n_components, 5)

    def test_print_topics(self):
        lda_model = self.modeler.fit_model()
        # Should not raise any exceptions
        try:
            self.modeler.print_topics(lda_model, 3)
        except Exception as e:
            self.fail(f"print_topics raised an exception: {e}")

if __name__ == '__main__':
    unittest.main()