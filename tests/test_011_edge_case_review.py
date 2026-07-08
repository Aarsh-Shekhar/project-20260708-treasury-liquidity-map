import unittest

from treasury_liquidity_map.models import Record
from treasury_liquidity_map.scoring import score_record


class DepthCheck11(unittest.TestCase):
    def test_011_edge_case_review(self):
        record = Record(id="cashflow-011", exposure=23545, signal=0.867, urgency=9)
        self.assertGreaterEqual(score_record(record), 0)
        self.assertLessEqual(score_record(record), 1)


if __name__ == "__main__":
    unittest.main()
