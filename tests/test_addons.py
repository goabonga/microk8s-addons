from utils import kubectl


class TestAddons(object):

    def test_nodes_is_not_empty(self):
        results = kubectl("get nodes")
        assert results != ""
