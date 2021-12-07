import unittest

from tf_idf import TfIdf


class TfIdfTestCase(unittest.TestCase):
    def test_tf(self):
        text = ['hasta', 'la', 'vista', 'baby', 'la', 'vista', 'la']
        expected_tf = {'la': 0.42857142857142855, 'vista': 0.2857142857142857,
                       'hasta': 0.14285714285714285, 'baby': 0.14285714285714285}
        self.assertEqual(expected_tf, TfIdf.compute_tf(text))

    def test_idf(self):
        texts = [['pasta', 'la', 'vista', 'baby', 'la', 'vista'],
         ['hasta', 'siempre', 'comandante', 'baby', 'la', 'siempre'],
         ['siempre', 'comandante', 'baby', 'la', 'siempre']]
        expected_idf = 0.47712125471966244
        self.assertEqual(expected_idf, TfIdf.compute_idf('pasta', texts))

    def test_tfidf(self):
        corpus = [['pasta', 'la', 'vista', 'baby', 'la', 'vista'],
            ['hasta', 'siempre', 'comandante', 'baby', 'la', 'siempre'],
            ['siempre', 'comandante', 'baby', 'la', 'siempre']]
        expected_tfidf = [{'pasta': 0.11928031367991561, 'baby': 0.0, 'vista': 0.23856062735983122, 'la': 0.0},
            {'hasta': 0.09542425094393249, 'comandante': 0.03521825181113625, 'siempre': 0.0704365036222725, 'baby': 0.0, 'la': 0.0},
            {'comandante': 0.04402281476392031, 'baby': 0.0, 'siempre': 0.08804562952784062, 'la': 0.0}]
        self.assertEqual(expected_tfidf, TfIdf.compute_tfidf(corpus))


if __name__ == '__main__':
    unittest.main()
